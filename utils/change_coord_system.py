from typing import Tuple


def change_coord_system(vector: Tuple[int, int, int], vector_start: Tuple[int, int, int],
                        point: Tuple[int, int, int]) -> Tuple[int, int, int]:
    new_coords = [point[0] - vector_start[0], point[1] - vector_start[1],
                  point[2] - vector_start[2]]

    vector_x_projection = [vector[0], vector[1]]
    vector_y_projection = [vector[0], vector[1]]
    vector_z_projection = [vector[0], vector[1]]
