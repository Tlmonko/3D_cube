from typing import Tuple, List

from cube import Cube
from utils import change_coord_system


def trace(screen_point: Tuple[float, float], cube: Cube) -> int:
    """Return number of edge which is cross by ray"""

    intersections_with_planes: List[Tuple[Tuple[float, float, float], int]] = []

    for plane_index in range(6):
        plane = cube.get_plane(plane_index)
        plane_coords = cube.get_plane_coords(plane_index)

        intersection = plane.ray_intersection(screen_point)
        if not intersection:
            continue

        start = plane_coords[-1]
        end = plane_coords[0]
        temp_axis = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
        new_point = change_coord_system(temp_axis, start, intersection)
        side = new_point[0] >= 0

        for node_index in range(len(plane_coords) - 1):
            start = plane_coords[node_index]
            end = plane_coords[node_index + 1]
            temp_axis = (end[0] - start[0], end[1] - start[1], end[2] - start[2])
            new_point = change_coord_system(temp_axis, start, intersection)
            temp_side = new_point[0] >= 0
            if temp_side != side:
                break
        else:
            intersections_with_planes.append((intersection, plane_index))
    if not intersections_with_planes:
        return -1
    print(intersections_with_planes)
    return min(intersections_with_planes, key=lambda intersection: intersection[1])[1]
