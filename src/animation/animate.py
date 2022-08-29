from functools import wraps
import math
import uuid

import bpy
from src.entities import AbstractBaseShape
from src.animation.structs import *

DURATION_TIME_TYPE = 1000  # Milliseconds


def use_multi_axis(method):
    """
    Wrapper method to allow passing multiple axis as string to our rotate, location, scale methods.
    Example:
        # Animates all the given axis with the values passed.
        scale('xyz', 5, start=0, end=500)

    :param method: Manipulation method (scale, rotate, location)
    :return: Animate() instance's self
    """
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        axis_input = method_args[0]

        # If more than one axis is provided, we loop through each of them and apply them individually.
        if len(axis_input) > 1:
            for axis in axis_input:
                # Overriding our args with the given axis.
                args = list(method_args)
                args[0] = axis
                method(self, *args, **method_kwargs)

            return self

        return method(self, *method_args, **method_kwargs)
    return _impl


class Animate:

    def __init__(self, entity: AbstractBaseShape, end_time=None):
        """
        Animation class that exposes basic methods to animate and manipulate the values of a given entity.

        :param entity: Any blender object that is wrapped inside an AbstractBaseShape class.
        :param end_time: (Optional) End time of the animation in seconds. If not set, the end time will be set
                         to the highest end time you provided in the animation methods.
        """
        self._entity = entity

        self.framerate = 24  # currently hardcoded

        self._end_frame = 0  # private getter for the end frame.
        self.end_frame = self._end_frame

        # if no end time given, the end time will be set to the highest end time that the user provides
        # when using animation methods (if dynamic_end is true).
        self.dynamic_end = True

        if end_time:
            self.dynamic_end = False
            self._end_frame = self._convert_ms_to_blender_frame(end_time)
            self.end_frame = self._end_frame

        self._entity.mesh.animation_data_create()
        self._entity.mesh.animation_data.action = bpy.data.actions.new(name=str(uuid.uuid4()))

        self._scale_axis_types = {
            "x": ScaleAxisX(),
            "y": ScaleAxisY(),
            "z": ScaleAxisZ(),
        }

        self._rotate_axis_types = {
            "x": RotateAxisX(),
            "y": RotateAxisY(),
            "z": RotateAxisZ(),
        }

        self._location_axis_types = {
            "x": LocationAxisX(),
            "y": LocationAxisY(),
            "z": LocationAxisZ(),
        }

        self._axis_types = [*self._scale_axis_types.values(), *self._rotate_axis_types.values(),
                            *self._location_axis_types.values()]

        self._curves = self._build_curves(self._axis_types)

        self._extrapolation = EXTRAPOLATION.CONSTANT

    def _build_curves(self, curves: list) -> dict:
        """
        Builds all base curves (scale, rotation, location) for our entity.
        This allows us to access the curves later for ease of use.

        :return: Dictionary where every key is corresponding to a blender data_path curve name.
        """
        curves_dict = {}

        for axis in curves:
            new_curve = self._entity.mesh.animation_data.action.fcurves.new(data_path=axis.data_path,
                                                                            index=axis.curve_idx)
            curves_dict[axis.curve_name] = new_curve

        return curves_dict

    @use_multi_axis
    def scale(self, axis, value, start, end) -> 'Animate':
        """
        Animation method that manipulates the entity's scale on one axis given a start and end point (in seconds).
        The method will, by default take the last value that was found in the axis curve as value to start animating
        from.

        :param axis: Axis as string (x, y, z).
        :param value: The scale value the entity should be manipulated towards the end time.
        :param start: Start time of the entity manipulation.
        :param end: Where the entity should be fully manipulated to it's given value.
        :return: self to enable a builder pattern.
        """
        scale_axis = self._scale_axis_types[axis]
        current_scale = self._entity.mesh.scale[scale_axis.curve_idx]

        self._manipulate_axis(scale_axis, current_scale, value, start, end)

        return self

    @use_multi_axis
    def rotate(self, axis, value, start, end, use_radians=False) -> 'Animate':
        """
        Animation method to manipulate the entity's rotation one one axis given a start and end point (in seconds).
        By default, the value is provided in degrees.

        :param axis: The rotation axis (x, y, z).
        :param value: Value the entity should be manipulated towards.
        :param start: Start time of rotation (in seconds).
        :param end: End time of rotation (in seconds).
        :param use_radians: If true, value is expected to be given in radians. No conversion is done.
        :return: self to enable a builder pattern.
        """
        rotate_axis = self._rotate_axis_types[axis]
        current_rotation = self._entity.mesh.rotation_euler[rotate_axis.curve_idx]

        value = value if use_radians else math.radians(value)

        self._manipulate_axis(rotate_axis, current_rotation, value, start, end)

        return self

    @use_multi_axis
    def location(self, axis, value, start, end) -> 'Animate':
        location_axis = self._location_axis_types[axis]
        current_location = self._entity.mesh.location[location_axis.curve_idx]

        self._manipulate_axis(location_axis, current_location, value, start, end)

        return self

    def _manipulate_axis(self, axis: Axis, start_val, end_val, start_sec, end_sec):
        start_keyframe = self._convert_ms_to_blender_frame(start_sec)
        end_keyframe = self._convert_ms_to_blender_frame(end_sec)

        curve = self._curves[axis.curve_name]

        if len(curve.keyframe_points) > 0:
            last_keyframe = curve.keyframe_points[-1]
            start_val = last_keyframe.co.y

        self._append_to_axis(axis, start_keyframe, start_val)
        self._append_to_axis(axis, end_keyframe, end_val)

        if self.dynamic_end and end_keyframe > self.end_frame:
            self.end_frame = end_keyframe

        return self

    def _append_to_axis(self, axis: Axis, keyframe: int, value) -> None:
        """
        Internally used to insert blender keyframes using structs.Axis.
        This cut's down some boilerplate and ensures a uniform, working insert of all axis structs.

        :param axis: Any axis of type Axis from the structs file.
        :param keyframe: The keyframe the value should be inserted at.
        :param value: The value that should be set on the specific keyframe
        :return:
        """
        curve = self._curves[axis.curve_name]
        curve.keyframe_points.insert(keyframe, value)

    def _convert_ms_to_blender_frame(self, milliseconds: int or float) -> int:
        """
        Converts milliseconds to the corresponding blender keyframe position.

        :param milliseconds: Integer value of milliseconds
        :return: Blender keyframe position
        """
        return int((milliseconds / DURATION_TIME_TYPE) * self.framerate)

    def _update_curve_extrapolation(self, value: EXTRAPOLATION) -> None:
        """
        Updates all curves with a given extrapolation.

        :param value: Blenders extrapolation options.
        :return:
        """

        for fc in self._curves.values():
            fc.extrapolation = value  # Set extrapolation type

            # Iterate over this fcurve's keyframes and set handles to vector
            for kp in fc.keyframe_points:
                kp.handle_left_type = 'VECTOR'
                kp.handle_right_type = 'VECTOR'

    @property
    def end_frame(self):
        return self._end_frame

    @end_frame.setter
    def end_frame(self, value: int):
        self._end_frame = value
        bpy.context.scene.frame_end = value  # setting the end frame inside blender

    @property
    def extrapolation(self):
        return self._extrapolation

    @extrapolation.setter
    def extrapolation(self, value: EXTRAPOLATION):
        self._extrapolation = value
        self._update_curve_extrapolation(value)
