from typing import Tuple, List

import numpy as np

from utils import calculate_distance


class Plane:
    normal: Tuple[int]
    edges: List[Tuple[int, int, int]]

    def __init__(self, coords: List[Tuple[int, int, int]]):
        first_vector = np.array([coords[0][0] - coords[1][0],
                                 coords[0][1] - coords[1][1], coords[0][2] - coords[1][2]])
        second_vector = np.array([coords[2][0] - coords[1][0],
                                  coords[2][1] - coords[1][1], coords[2][2] - coords[1][2]])
        result = np.cross(first_vector, second_vector)
        self.normal = tuple(result.tolist())

        edges_points = []

        for node in coords:
            for second_node in coords:
                if abs(int(calculate_distance(node, second_node)) - 200) <= 2:
                    edges_points.append((node, second_node))
        edges = []

    def ray_intersection(direction_vector: Tuple[int, int, int]) -> bool:
        pass
