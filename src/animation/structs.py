from abc import ABC
from dataclasses import dataclass


class EXTRAPOLATION:

    CONSTANT = 'CONSTANT'
    LINEAR = 'LINEAR'


class Axis(ABC):

    data_path: str
    curve_name: str
    curve_idx: int


@dataclass
class ScaleAxisX(Axis):

    data_path = 'scale'
    curve_name = 'scale_x'
    curve_idx = 0


@dataclass
class ScaleAxisY(Axis):

    data_path = 'scale'
    curve_name = 'scale_y'
    curve_idx = 1


@dataclass
class ScaleAxisZ(Axis):

    data_path = 'scale'
    curve_name = 'scale_z'
    curve_idx = 2


@dataclass
class RotateAxisX(Axis):

    data_path = 'rotation_euler'
    curve_name = 'rotate_x'
    curve_idx = 0


@dataclass
class RotateAxisY(Axis):

    data_path = 'rotation_euler'
    curve_name = 'rotate_y'
    curve_idx = 1


@dataclass
class RotateAxisZ(Axis):

    data_path = 'rotation_euler'
    curve_name = 'rotate_z'
    curve_idx = 2


@dataclass
class LocationAxisX(Axis):

    data_path = 'location'
    curve_name = 'location_x'
    curve_idx = 0


@dataclass
class LocationAxisY(Axis):

    data_path = 'location'
    curve_name = 'location_y'
    curve_idx = 1


@dataclass
class LocationAxisZ(Axis):
    data_path = 'location'
    curve_name = 'location_z'
    curve_idx = 2