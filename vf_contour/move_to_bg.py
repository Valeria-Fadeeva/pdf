#!/usr/bin/env python3
"""Главный файл модуля page_recognition"""


import os
import sys
import cv2 as cv
import numpy as np
from math import floor

sys.path.append("..")
from vf_base.mkpath import mkpath
from vf_base.scan_dir_os import scan_dir_os
from vf_base.scan_dir_os import scan_files_os


def bg_img(h, w, color_fill = 255):
    img = np.zeros([h, w, 3], dtype=np.uint8)
    img.fill(255)
    # or img[:] = 255
    return img


def combine_img(src_img, bg):
    src_img_h, src_img_w = src_img.shape[:2]
    res_img_h, res_img_w = bg.shape[:2]

    y_offset, x_offset = (floor((res_img_h - src_img_h) / 2), floor((res_img_w - src_img_w) / 2))

    bg[y_offset:y_offset + src_img_h, x_offset:x_offset + src_img_w] = src_img

    return bg


def move_to_bg(subproject, config, filepath=False):
    """Главная функция модуля page_recognition"""

    # subproject dir
    subproject_path = os.path.abspath(os.path.join(
        config.get('project'), config.get('scan'), subproject))
    mkpath(subproject_path)

    # subproject result dir
    subproject_result_path = os.path.abspath(os.path.join(
        config.get('project'), config.get('split'), subproject))
    mkpath(subproject_result_path)

    # main _result dirs
    subproject_result_main_path = os.path.abspath(os.path.join(
        subproject_result_path, config.get('subproject').get('main')))

    subproject_result_main_format_path = os.path.abspath(
        os.path.join(subproject_result_main_path, config.get('format')))
    mkpath(subproject_result_main_format_path)

    # получить список png или jpg файлов в папке png или jpg см. config.get('format')
    fso_result_main_format = scan_dir_os(subproject_result_main_format_path)

    # получить обработанные изображения, поместить на фон и сохранить обратно

    src_img_h_max, src_img_w_max = (None, None)
    print("Считаем максимальные размеры изображений")
    for f in fso_result_main_format:
        # прочитать файл изображения
        src_image = cv.imread(f, cv.IMREAD_COLOR)
        src_img_h, src_img_w = src_image.shape[:2]

        if src_img_h_max is None and src_img_w_max is None:
            src_img_h_max, src_img_w_max = src_image.shape[:2]
        else:
            if src_img_h > src_img_h_max:
                src_img_h_max = src_img_h

            if src_img_w > src_img_w_max:
                src_img_w_max = src_img_w

    res_img_h, res_img_w = ([floor(src_img_h_max + src_img_h_max * 0.1), floor(src_img_w_max + src_img_w_max * 0.1)])
    bg = bg_img(res_img_h, res_img_w)

    print("Помещаем изображения на фон")
    for f in fso_result_main_format:
        print(f)
        # прочитать файл изображения
        src_image = cv.imread(f, cv.IMREAD_COLOR)

        img = combine_img(src_image, bg.copy())

        cv.imwrite(f, img)
        print("Готово")

    return True
