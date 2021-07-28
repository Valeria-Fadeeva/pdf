#!/usr/bin/env python3
"""Файл получения четырехугольника"""


import sys
from typing import Any
import numpy as np

sys.path.append("..")
from vf_base.digits import dict_int_range_search


def get_quadrangle_vertices(points_arr: list, mode: int = 1) -> list | Any | None:
    """Функция получения четырехугольника"""
    if len(points_arr) <= 2:
        return None

    # словарь: иксы являются индексами и хранят игреки
    dx = {}
    for i in points_arr:
        sx = dict_int_range_search(dx, i[0]-50, i[0]+50)
        if sx is None:
            dx[i[0]] = []
            dx[i[0]].append(i[1])
        else:
            dx[sx[0][0]].append(i[1])

    # для каждого значения в dx, если индекс хранит 2 или больше значений
    # словарь: иксы являются индексами и хранят игреки, но таких иксов уже меньше
    dx2p = {}
    for i in dx:
        if len(dx[i]) >= 2:
            dx2p[i] = dx[i]

    min_x1 = min(dx2p)
    max_x1 = max(dx2p)
    #min_x2 = min(dx2p)
    max_x2 = max(dx2p)

    min_y1 = min(dx2p[min_x1])
    max_y1 = max(dx2p[min_x1])
    min_y2 = min(dx2p[max_x1])
    max_y2 = max(dx2p[max_x1])

    vertices = [[min_x1, min_y1], [min_x1, max_y1], [max_x2, max_y2], [max_x1, min_y2]]
    if mode == 1:
        return vertices
    else:
        vertices = np.array(vertices)
        return vertices
