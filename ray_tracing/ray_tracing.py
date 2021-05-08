from typing import Tuple, List

from cube import Cube
from utils import in_polygon


def trace(screen_point: Tuple[float, float], cube: Cube) -> int:
    """Return number of edge which is cross by ray"""

    intersections_with_planes: List[Tuple[Tuple[float, float, float], int]] = []

    for plane_index in range(6):
        plane = cube.get_plane(plane_index)
        plane_coords = cube.get_plane_coords(plane_index)

        intersection = plane.ray_intersection(screen_point)
        if not intersection:
            continue

        if in_polygon(screen_point[0], screen_point[1], [coord[0] for coord in plane_coords],
                      [coord[2] for coord in plane_coords]):
            intersections_with_planes.append((intersection, plane_index))

    if not intersections_with_planes:
        return -1
    return min(intersections_with_planes, key=lambda intersection: intersection[0][1])[1]
