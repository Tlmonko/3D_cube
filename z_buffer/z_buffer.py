from typing import List, Tuple


class ZBuffer:
    buffer: List[List[float]]
    screen: List[List[str]]
    width: int
    height: int
    background_color: str

    def __init__(self, width: int, height: int, background_color: str) -> None:
        self.buffer = [[float('+inf')] * width for el in range(height)]
        self.screen = [[background_color] * width for el in range(height)]
        self.width = width
        self.height = height
        self.background_color = background_color

    def add_points(self, points: List[Tuple[int, int, int]], color: str) -> None:
        for point in points:
            if point[1] < self.buffer[point[2] + self.height // 2][point[0] + self.width // 2]:
                self.buffer[point[2] + self.height // 2][point[0] + self.width // 2] = point[1]
                self.screen[point[2] + self.height // 2][point[0] + self.width // 2] = color

    def get_screen(self) -> List[List[str]]:
        return self.screen

    def update(self):
        self.buffer = [[float('+inf')] * self.width for el in range(self.height)]
        self.screen = [[self.background_color] * self.width for el in range(self.height)]
