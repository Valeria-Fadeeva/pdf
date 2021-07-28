#!/usr/bin/env python3
"""Файл получения прямоугольника"""


from typing import Any
import numpy as np


def get_rectangle_vertices(points_arr: list, mode: int = 1) -> Any:
    """Функция получения прямоугольника"""
    d = {}
    for i in points_arr:
        d[i[0]+i[1]] = i

    min_x_y = d[min(d)]
    max_x_y = d[max(d)]
    min_x_max_y = [min_x_y[0], max_x_y[1]]
    max_x_min_y = [max_x_y[0], min_x_y[1]]

    vertices = [min_x_y, min_x_max_y, max_x_y, max_x_min_y]
    if mode == 1:
        return vertices
    else:
        vertices = np.array(vertices)
        return vertices
