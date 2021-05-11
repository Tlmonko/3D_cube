from math import radians
from typing import List, Tuple

from utils import rotate_z, rotate_y, rotate_x, Plane


class Cube:
    center: Tuple[float, float, float]
    nodes: List[Tuple[int, int, int]]
    rotation: List[int]
    planes_points: List[List[int]]
    planes: List[Plane]

    def __init__(self) -> None:
        self.center = (0.0, 0.0, 0.0)
        self.calculate_nodes()
        self.rotation = [0, 0, 0]
        self.init_planes()

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

        self.planes_points = [
            [6, 4, 5, 7],
            [7, 3, 2, 6],
            [2, 3, 1, 0],
            [0, 4, 5, 1],
            [7, 5, 1, 3],
            [6, 4, 0, 2]
        ]

    def rotate(self, angle_x: int, angle_y: int, angle_z: int) -> None:
        self.rotation[0] += angle_x
        self.rotation[1] += angle_y
        self.rotation[2] += angle_z
        for node in range(len(self.nodes)):
            self.nodes[node] = rotate_z(self.nodes[node], radians(angle_z))
            self.nodes[node] = rotate_x(self.nodes[node], radians(angle_x))
            self.nodes[node] = rotate_y(self.nodes[node], radians(angle_y))
        self.update_planes()

    def get_plane_coords(self, number: int) -> List[Tuple[float, float, float]]:
        return [self.nodes[node] for node in self.planes_points[number]]

    def init_planes(self) -> None:
        self.planes = []
        for plane_index in range(6):
            plane = Plane(self.get_plane_coords(plane_index))
            self.planes.append(plane)

    def update_planes(self) -> None:
        for plane_index in range(6):
            self.planes[plane_index].update(self.get_plane_coords(plane_index))

    def get_plane(self, number: int) -> Plane:
        return self.planes[number]

    def rasterize_plane(self, number: int) -> List[Tuple[int, int, int]]:
        plane_coords = self.get_plane_coords(number)
        plane = self.get_plane(number)
        coords = plane_coords.copy()
        top_point_index = coords.index(max(coords, key=lambda coord: coord[2]))
        top_point = coords.pop(top_point_index)
        bottom_point_index = coords.index(min(coords, key=lambda coord: coord[2]))
        bottom_point = coords.pop(bottom_point_index)
        left_point = min(coords, key=lambda coord: coord[0])
        right_point = max(coords, key=lambda coord: coord[0])
        if right_point == top_point or right_point == bottom_point:
            return []
        if len([coord for coord in plane_coords if coord[2] == top_point[2]]) > 1:
            top_points = [point for point in plane_coords if point[2] == top_point[2]]
            bottom_points = [point for point in plane_coords if point[2] == bottom_point[2]]
            left_points = [min(top_points, key=lambda point: point[0]),
                           min(bottom_points, key=lambda point: point[0])]
            right_points = [max(top_points, key=lambda point: point[0]),
                            max(bottom_points, key=lambda point: point[0])]
            # print(left_points, right_points, top_points, bottom_points)
            if left_points[0][2] == left_points[1][2]:
                k1 = 0
            else:
                k1 = (left_points[1][0] - left_points[0][0]) / (
                        left_points[1][2] - left_points[0][2])
            b1 = left_points[0][0] - k1 * left_points[0][2]
            if right_points[0][2] == right_points[1][2]:
                k2 = 0
            else:
                k2 = (right_points[1][0] - right_points[0][0]) / (
                        right_points[1][2] - right_points[0][2])
            b2 = right_points[0][0] - k2 * right_points[0][2]
            result = []
            # print(k1, b1, k2, b2)
            for y in range(int(bottom_point[2]), int(top_point[2])):
                for x in range(int(k1 * y + b1), int(k2 * y + b2)):
                    result.append((x, -(
                            plane.normal[0] * x + plane.normal[2] * y + plane.coefficient) /
                                   plane.normal[1], y))
            return result
        else:
            """Lines numerating from 1 to 4 by clockwise from bottom left"""
            if bottom_point[2] == left_point[2]:
                k1 = 0
            else:
                k1 = (bottom_point[0] - left_point[0]) / (bottom_point[2] - left_point[2])
            if left_point[2] == top_point[2]:
                k2 = 0
            else:
                k2 = (left_point[0] - top_point[0]) / (left_point[2] - top_point[2])
            if top_point[2] == right_point[2]:
                k3 = 0
            else:
                k3 = (top_point[0] - right_point[0]) / (top_point[2] - right_point[2])
            if right_point[2] == bottom_point[2]:
                k4 = 0
            else:
                k4 = (right_point[0] - bottom_point[0]) / (right_point[2] - bottom_point[2])
            b1 = bottom_point[0] - k1 * bottom_point[2]
            b2 = left_point[0] - k2 * left_point[2]
            b3 = top_point[0] - k3 * top_point[2]
            b4 = right_point[0] - k4 * right_point[2]
            result = []
            for y in range(int(bottom_point[2]), int(top_point[2])):
                for x in range(int(max(k1 * y + b1, k2 * y + b2)),
                               int(min(k3 * y + b3, k4 * y + b4))):
                    result.append((x, -(
                            plane.normal[0] * x + plane.normal[2] * y + plane.coefficient) /
                                   plane.normal[1], y))
            return result


if __name__ == '__main__':
    cube = Cube()
    print(cube.rasterize_plane(1))
