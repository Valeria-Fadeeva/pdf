#!/usr/bin/env python3
"""Проверка файла на наличие"""


import os


def check_file(obj):
    """Функция проверки файла на наличие"""

    return bool(os.path.exists(obj))
