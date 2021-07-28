#!/usr/bin/env python3
"""Файл функций отображения содержимого каталога"""


from pathlib import Path


def scan_files_pathlib(p):
    """Функция отображения содержимого каталога"""
    pobj = Path(p)
    paths = []

    for child in pobj.iterdir():
        if child.is_file():
            if '.pdf' in child.name:
                paths.append(child)
            if '.png' in child.name:
                paths.append(child)
            if '.jpg' in child.name:
                paths.append(child)

    return paths


def scan_dir_pathlib(p):
    """Функция отображения содержимого каталога"""
    pobj = Path(p)
    paths = []

    for child in pobj.iterdir():
        if child.is_dir():
            paths.append([child, scan_files_pathlib(child)])
        elif child.is_file():
            if '.pdf' in child.name:
                paths.append(child)
            if '.png' in child.name:
                paths.append(child)
            if '.jpg' in child.name:
                paths.append(child)

    return paths
