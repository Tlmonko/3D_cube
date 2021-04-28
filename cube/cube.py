from typing import List, Tuple
from utils import rotate_z, rotate_y, rotate_x


class Cube:
    center: Tuple[int, int, int]
    nodes: List[Tuple[int, int, int]]

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

    def rotate(self, angle_x: int, angle_y: int, angle_z: int) -> None:
        for node in range(len(self.nodes)):
            self.nodes[node] = rotate_z(self.nodes[node], angle_z)
            self.nodes[node] = rotate_x(self.nodes[node], angle_x)
            self.nodes[node] = rotate_y(self.nodes[node], angle_y)
