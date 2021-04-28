import numpy as np
from typing import Tuple
from math import cos, sin, radians


def rotate_z(vector: Tuple[int, int, int], angle: int):
    """Rotating vector around z axis by a given angle (in degrees)"""
    angle = radians(angle)
    vector_np = np.matrix(list(vector))
    rotation_matrix = np.matrix([
        [cos(angle), sin(angle), 0],
        [-sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    result = np.dot(vector_np, rotation_matrix).tolist()
    return result[0][0], result[0][1], result[0][2]


def rotate_x(vector: Tuple[int, int, int], angle: int):
    """Rotating vector around y axis by a given angle (in degrees)"""
    angle = radians(angle)
    vector_np = np.matrix(list(vector))
    rotation_matrix = np.matrix([
        [cos(angle), 0, -sin(angle)],
        [0, 1, 0],
        [sin(angle), 0, cos(angle)]
    ])
    result = np.dot(vector_np, rotation_matrix).tolist()
    return result[0][0], result[0][1], result[0][2]

def rotate_y(vector: Tuple[int, int, int], angle: int):
    """Rotating vector around y axis by a given angle (in degrees)"""
    angle = radians(angle)
    vector_np = np.matrix(list(vector))
    rotation_matrix = np.matrix([
        [1, 0, 0],
        [0, cos(angle), sin(angle)],
        [0, -sin(angle), cos(angle)]
    ])
    result = np.dot(vector_np, rotation_matrix).tolist()
    return result[0][0], result[0][1], result[0][2]