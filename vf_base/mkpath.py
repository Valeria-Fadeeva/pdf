#!/usr/bin/env python3
"""Файл создания каталога, если он не существует"""


import os


def mkpath(p):
    """Функция создания каталога, если он не существует"""
    if not os.path.exists(p):
        return os.makedirs(p)
