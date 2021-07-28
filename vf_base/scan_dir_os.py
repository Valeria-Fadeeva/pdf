#!/usr/bin/env python3
"""Файл функций отображения содержимого каталога"""


import os


def scan_files_os(p):
    """Функция отображения содержимого каталога"""
    p = os.path.abspath(p)
    pobj = [os.path.abspath(os.path.join(p, x)) for x in os.listdir(p)]
    paths = []

    for child in pobj:
        if os.path.isfile(child):
            if '.pdf' in child:
                paths.append(child)
            if '.png' in child:
                paths.append(child)
            if '.jpg' in child:
                paths.append(child)

    return paths


def scan_dir_os(p):
    """Функция отображения содержимого каталога"""
    p = os.path.abspath(p)
    pobj = [os.path.abspath(os.path.join(p, x)) for x in os.listdir(p)]
    paths = []
    
    for child in pobj:
        if os.path.isdir(child):
            paths.append([child, scan_files_os(child)])
        elif os.path.isfile(child):
            if '.pdf' in child:
                paths.append(child)
            if '.png' in child:
                paths.append(child)
            if '.jpg' in child:
                paths.append(child)
    
    return paths
