from math import acos
from typing import Tuple

from utils import rotate_z, rotate_y


def change_coord_system(vector: Tuple[float, float, float],
                        vector_start: Tuple[float, float, float],
                        point: Tuple[float, float, float]) -> Tuple[float, float, float]:
    point = (point[0] - vector_start[0], point[1] - vector_start[1],
             point[2] - vector_start[2])

    cos_between_x_and_vector = vector[0] / (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    point = rotate_z(point, acos(cos_between_x_and_vector))
    cos_between_z_and_vector = vector[2] / (vector[0] ** 2 + vector[2] ** 2) ** 0.5
    point = rotate_y(point, -acos(cos_between_z_and_vector))
    return point


if __name__ == '__main__':
    vector_test = (2, 0, 0)
    point_test = (2, 0, -2)
    point_new = change_coord_system(vector_test, (0, 0, 0), point_test)
    print(point_new)
