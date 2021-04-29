from typing import Tuple


def calculate_distance(first_coords: Tuple[int, int, int],
                       second_coords: Tuple[int, int, int]) -> float:
    return ((first_coords[0] - second_coords[0]) ** 2 + (
                first_coords[1] - second_coords[1]) ** 2 + (
                        first_coords[2] - second_coords[2]) ** 2) ** (1 / 2)
