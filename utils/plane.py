from typing import Tuple, List

import numpy as np

from utils import calculate_distance


class Plane:
    normal: Tuple[float]
    coefficient: float
    edges: List[Tuple[float, float, float]]

    def __init__(self, coords: List[Tuple[float, float, float]]):
        first_vector = np.array([coords[0][0] - coords[1][0],
                                 coords[0][1] - coords[1][1], coords[0][2] - coords[1][2]])
        second_vector = np.array([coords[2][0] - coords[1][0],
                                  coords[2][1] - coords[1][1], coords[2][2] - coords[1][2]])
        result = np.cross(first_vector, second_vector)
        self.normal = tuple(result.tolist())
        self.coefficient = -(
                self.normal[0] * coords[3][0] + self.normal[1] * coords[3][1] + self.normal[2] *
                coords[3][2])

        edges_points = []

        for node in coords:
            for second_node in coords:
                if abs(int(calculate_distance(node, second_node)) - 200) <= 2:
                    edges_points.append((node, second_node))

    def ray_intersection(self, point: Tuple[float, float]) -> Tuple[float, float, float]:
        if self.normal[3] == 0:
            return ()
        z_coord: float = (self.normal[0] * point[0] + self.normal[1] * point[
            1] + self.coefficient) / self.normal[2]
        return point[0], point[1], z_coord
