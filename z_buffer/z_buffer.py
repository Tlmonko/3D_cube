from typing import List, Tuple

import numpy as np


class ZBuffer:
    buffer: np.ndarray
    screen: np.ndarray
    width: int
    height: int
    background_color: Tuple[int, int, int]

    def __init__(self, width: int, height: int, background_color: Tuple[int, int, int]) -> None:
        self.buffer = np.empty((width, height))
        self.screen = np.empty((width, height, 3))
        self.default_buffer = np.empty((width, height))
        self.default_screen = np.empty((width, height, 3))
        for i in range(width):
            for j in range(height):
                self.default_buffer[i][j] = float('+inf')
                self.default_screen[i][j] = background_color
        self.width = width
        self.height = height
        self.background_color = background_color
        self.update()

    def add_points(self, points: List[Tuple[int, int, int]], color: Tuple[int, int, int]) -> None:
        for point in points:
            if point[1] <= self.buffer[point[0] + self.width // 2][point[2] + self.height // 2]:
                self.buffer[point[0] + self.width // 2][point[2] + self.height // 2] = point[1]
                self.screen[point[0] + self.width // 2][point[2] + self.height // 2] = color

    def get_screen(self) -> np.ndarray:
        return self.screen

    def update(self):
        self.buffer = self.default_buffer.copy()
        self.screen = self.default_screen.copy()
