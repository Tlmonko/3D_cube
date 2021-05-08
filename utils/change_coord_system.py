from math import acos, copysign
from typing import Tuple

from .rotation_matrix import rotate_z, rotate_y, rotate_x


def change_coord_system(vector: Tuple[float, float, float],
                        vector_start: Tuple[float, float, float],
                        point: Tuple[float, float, float]) -> Tuple[float, float, float]:
    point = (point[0] - vector_start[0], point[1] - vector_start[1],
             point[2] - vector_start[2])
    cos_between_x_and_vector = vector[0] / (vector[0] ** 2 + vector[1] ** 2) ** 0.5 if vector[0] ** 2 + vector[1] ** 2 != 0 else 1
    cos_between_z_and_vector = vector[2] / (vector[0] ** 2 + vector[2] ** 2) ** 0.5 if vector[0] ** 2 + vector[2] ** 2 != 0 else 1
    coefficient_x = copysign(1, vector[1]) if vector[1] != 0 else 0
    coefficient_z = copysign(1, vector[0])
    point = rotate_z(point, coefficient_x * acos(cos_between_x_and_vector))
    point = rotate_y(point, coefficient_z * -acos(cos_between_z_and_vector))
    return point[0], point[1], point[2]


if __name__ == '__main__':
    vector_test = (0, 1, 0)
    point_test = (1, 1, 1)
    point_new = change_coord_system(vector_test, (0, 0, 0), point_test)
    print(point_new)
