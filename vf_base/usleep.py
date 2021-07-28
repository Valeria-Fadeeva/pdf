#!/usr/bin/env python3
"""Файл паузы"""


from time import sleep


def usleep(x):
    """Функция паузы в милисекундах"""
    return sleep(x/1000000.0)
