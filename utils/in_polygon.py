from typing import List, Tuple


def in_polygon(x: float, y: float, points: List[Tuple[float, float]]) -> bool:
    signes = []
    for i in range(-1, len(points) - 1):
        signes.append((x - points[i][0]) * (points[i + 1][1] - points[i][1]) - (points[i + 1][0] - points[i][0]) * (
                    y - points[i][1]) > 0)
    return all(signes) or not any(signes)
