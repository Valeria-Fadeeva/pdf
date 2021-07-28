#!/usr/bin/env python3
"""Файл получения четырехугольника"""


from typing import Any
import numpy as np


def get_quadrangle_vertices(points_arr: list, mode: int = 1) -> Any:
    """Функция получения четырехугольника"""
    d = {}
    for i in points_arr:
        d[i[0]+i[1]] = i

    min_x_y = d[min(d)]
    max_x_y = d[max(d)]

    min_x_max_y = None
    max_x_min_y = None

    for i in points_arr:
        if i[0] in range(min_x_y[0] - 50, min_x_y[0] + 50):
            if i[1] in range(max_x_y[1] - 50, max_x_y[1] + 50):
                min_x_max_y = i

    for i in points_arr:
        if i[0] in range(max_x_y[0] - 50, max_x_y[0] + 50):
            if i[1] in range(min_x_y[1] - 50, min_x_y[1] + 50):
                max_x_min_y = i

    if min_x_max_y is None:
        min_x_max_y = [min_x_y[0], max_x_y[1]]

    if max_x_min_y is None:
        max_x_min_y = [max_x_y[0], min_x_y[1]]

    vertices = [min_x_y, min_x_max_y, max_x_y, max_x_min_y]

    if mode == 1:
        return vertices
    else:
        vertices = np.array(vertices)
        return vertices
