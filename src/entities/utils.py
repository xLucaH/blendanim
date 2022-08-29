import mathutils


def get_min_max_points(points):
    x_coordinates, y_coordinates, z_coordinates = zip(*points)

    return [(min(x_coordinates), min(y_coordinates), min(z_coordinates)),
            (max(x_coordinates), max(y_coordinates), max(z_coordinates))]


def get_bounding_box(mesh):
    points = [mesh.matrix_world @ mathutils.Vector(corner) for corner in mesh.bound_box]

    return get_min_max_points(points)
