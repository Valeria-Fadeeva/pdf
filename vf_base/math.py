#!/usr/bin/env python3
"""Файл математических, геометрических функций"""


import math


def get_distance(**kwargs) -> int | float | bool:
    """
    Функция рассчета дистанции

    Keyword arguments:

    x1: int, y1: int, x2: int, y2: int

    or

    xy1: list[int], xy2: list[int]

    Return: distance: int
    """

    if kwargs.get('x1') is not None and kwargs.get('x2') is not None and kwargs.get('y1') is not None and kwargs.get('y2') is not None:
        dist = math.sqrt(
            (kwargs.get('x2') - kwargs.get('x1'))**2 +
            (kwargs.get('y2') - kwargs.get('y1'))**2
        )
    elif kwargs.get('xy1') is not None and kwargs.get('xy2') is not None:
        dist = math.sqrt(
            (kwargs.get('xy2')[0] - kwargs.get('xy1')[0])**2 +
            (kwargs.get('xy2')[1] - kwargs.get('xy1')[1])**2
        )

    if 'dist' in locals():
        return dist
    else:
        return False
