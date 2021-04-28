from typing import Tuple
import numpy as np


class Plane:
    normal: Tuple[int]

    def __init__(self, first_coords: Tuple[int, int, int], second_coords: Tuple[int, int, int], third_coords: Tuple[int, int, int]):
        first_vector = np.array([first_coords[0] - second_coords[0],
                                first_coords[1] - second_coords[1], first_coords[2] - second_coords[2]])
        second_vector = np.array([third_coords[0] - second_coords[0],
                                  third_coords[1] - second_coords[1], third_coords[2] - second_coords[2]])
        result = np.cross(first_vector, second_vector)
        self.normal = tuple(result.tolist())
