from abc import ABC, abstractmethod

import bpy

from . import utils


class AbstractBaseShape(ABC):

    def __init__(self, mesh):
        self._mesh = mesh

    @property
    def mesh(self):
        return self._mesh

    @abstractmethod
    def scale(self, x: float or int = None, y: float or int = None, z: float or int = None):
        """
        Scales the given shape by a given value

        :param x:
        :param y:
        :param z:
        :return:
        """
        pass

    def get_bounding_box(self):
        return utils.get_bounding_box(self._mesh)


class Cube(AbstractBaseShape):

    def __init__(self, width: int, height: int):
        self.initial_width = width
        self.initial_height = height

        bpy.ops.mesh.primitive_cube_add(scale=[self.initial_width,  # x-axis
                                               self.initial_width,  # y-axis (not height)
                                               self.initial_height])  # z-axis (this is the height)
        super().__init__(bpy.context.active_object)

    def scale(self, x: float or int = None, y: float or int = None, z: float or int = None):
        original_scale = self._mesh.scale
        new_scale = (x or original_scale[0], y or original_scale[1], z or original_scale[2])
        self._mesh.scale = new_scale
