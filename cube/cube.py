from typing import List, Tuple
from utils import rotate_z, rotate_y, rotate_x


class Cube:
    center: Tuple[int, int, int]
    nodes: List[Tuple[int, int, int]]
    planes: List[List[int]]

    def __init__(self) -> None:
        self.center = (0, 0)
        self.calculate_nodes()

    def calculate_nodes(self) -> None:
        self.nodes = [
            (100, 100, 100),
            (100, 100, -100),
            (100, -100, 100),
            (100, -100, -100),
            (-100, 100, 100),
            (-100, 100, -100),
            (-100, -100, 100),
            (-100, -100, -100)
        ]

        self.planes = [
            [6, 4, 5, 7],
            [7, 3, 2, 6],
            [2, 3, 1, 0],
            [0, 4, 5, 1],
            [7, 5, 1, 3],
            [6, 4, 0, 2]
        ]

    def rotate(self, angle_x: int, angle_y: int, angle_z: int) -> None:
        for node in range(len(self.nodes)):
            self.nodes[node] = rotate_z(self.nodes[node], angle_z)
            self.nodes[node] = rotate_x(self.nodes[node], angle_x)
            self.nodes[node] = rotate_y(self.nodes[node], angle_y)

    def get_plane(self, number: int) -> List[Tuple[int, int, int]]:
        return [self.nodes[node] for node in self.planes[number]]
