import os
from abc import ABC, abstractmethod

import bpy

from . import utils


class AbstractBaseShape(ABC):

    def __init__(self, mesh):
        self._mesh = mesh

    @property
    def mesh(self):
        return self._mesh

    def get_bounding_box(self):
        return utils.get_bounding_box(self._mesh)


class ImportShape(AbstractBaseShape):
    """
    Imports a 3D file from a filepath and wraps it around the AbstractBaseShape class.
    """

    import_operations = {
        ".obj": bpy.ops.import_scene.obj,
        ".dae": bpy.ops.import_scene.dae,
        ".blend": bpy.ops.import_scene.blend,
        ".fbx": bpy.ops.import_scene.fbx,
        ".ply": bpy.ops.import_mesh.ply,
        ".wrl": bpy.ops.import_scene.wrl,
        ".x3d": bpy.ops.import_scene.x3d,
        '.glb': bpy.ops.import_scene.glb,
        '.gltf': bpy.ops.import_scene.gltf,
        ".stl": bpy.ops.import_mesh.stl

    }

    def __init__(self, filepath: str):
        self.filepath = filepath

        super().__init__(self._import(self.filepath))

    def _import(self, filepath: str):
        filename, file_extension = os.path.splitext(filepath)

        import_operation = self.import_operations[file_extension]
        import_operation(filepath=filepath)

        return bpy.context.active_object


class Cube(AbstractBaseShape):

    def __init__(self, width: int, height: int):
        self.initial_width = width
        self.initial_height = height

        bpy.ops.mesh.primitive_cube_add(scale=[self.initial_width,  # x-axis
                                               self.initial_width,  # y-axis (not height)
                                               self.initial_height])  # z-axis (this is the height)
        super().__init__(bpy.context.active_object)
