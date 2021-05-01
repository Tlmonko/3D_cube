from typing import Tuple

from cube import Cube


def trace(screen_point: Tuple[int, int], cube: Cube) -> int:
    """Return number of edge which is cross by ray"""

    for plane_index in range(6):
        plane = cube.get_plane(plane_index)
        plane_coords = cube.get_plane_coords(plane_index)

        intersection = plane.ray_intersection(screen_point)




