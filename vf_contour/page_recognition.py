#!/usr/bin/env python3
"""Главный файл модуля page_recognition"""


import os
import sys
from pdf2image import convert_from_path
import cv2 as cv
import numpy as np
from math import floor

from .image import image_prepare, image_prepare_alt
from .contour import get_contours
from .page import page_process

sys.path.append("..")
from vf_base.digits import get_cnt_num_from_string, str_to_int
from vf_base.mkpath import mkpath
from vf_base.scan_dir_os import scan_dir_os
from vf_base.scan_dir_os import scan_files_os


def _main(image_src: np.ndarray, mode: int = 2, start=150, end=255, debug=False) -> list:
    """Главная функция модуля page_recognition"""

    image = image_prepare(image_src, start, end, debug=debug)
    if not isinstance(image, np.ndarray):
        raise RuntimeError('Картинки не обработались')

    contours = get_contours(image, mode)
    if not isinstance(contours, list) and len(contours) <= 1:
        raise RuntimeError('Контуры не найдены')

    images_array = page_process(image_src, contours, debug=debug)
    if not isinstance(images_array, list):
        raise RuntimeError('Картинки не получены')

    return images_array


def _main_alt(image_src: np.ndarray, mode: int = 2, start=150, end=255, debug=False) -> list:
    """Главная функция модуля page_recognition"""

    image = image_prepare_alt(image_src, start, end, debug=debug)
    if not isinstance(image, np.ndarray):
        raise RuntimeError('Картинки не обработались')

    contours = get_contours(image, mode)
    if not isinstance(contours, list) and len(contours) <= 1:
        raise RuntimeError('Контуры не найдены')

    images_array = page_process(image_src, contours, debug=debug)
    if not isinstance(images_array, list):
        raise RuntimeError('Картинки не получены')

    return images_array


def get_result_name(result_path, dig):
    # просканировать каталог с результатами
    result_files = scan_files_os(result_path)

    if not result_files:
        # если файлов нет, первый файл начинается с 0, имеет формат числа с ведущими нулями от количества разрядов источника
        n = 0
        f = '{:{fill}{align}{width}}'.format(n, fill=0, align='>', width=dig)
        return f
    else:
        # если файлы есть, определить число в имени последнего файла, добавить единицу, формат числа с ведущими нулями от количества разрядов источника
        n = int(str(os.path.basename(result_files[-1]).split('.')[0]))+1
        f = '{:{fill}{align}{width}}'.format(n, fill=0, align='>', width=dig)
        return f


def get_result_images(image, debug=False):
    img_list = False

    start = 150
    while not img_list and start > 0:
        img_list = _main(image, start=start, debug=debug)
        if not img_list:
            start -= 10

    start = 250
    while not img_list and start > 150:
        img_list = _main(image, start=start, debug=debug)
        if not img_list:
            start -= 10

    start = 150
    while not img_list and start > 0:
        img_list = _main_alt(image, start=start, debug=debug)
        if not img_list:
            start -= 10

    start = 250
    while not img_list and start > 150:
        img_list = _main_alt(image, start=start, debug=debug)
        if not img_list:
            start -= 10

    #if not img_list:
    #    height = 800
    #    width = 800
    #    blank_img = np.zeros((height, width, 3), np.uint8)
    #    img_list = []
    #    img_list.append(blank_img)

    if not img_list:
        img_list = []
        img_list.append(image)

    return img_list


def page_recognition(subproject, config, filepath=False):
    """Главная функция модуля page_recognition"""

    # subproject dir
    subproject_path = os.path.abspath(os.path.join(
        config.get('project'), config.get('scan'), subproject))
    mkpath(subproject_path)

    # start dirs
    subproject_start_pdf_path = os.path.abspath(os.path.join(
        subproject_path, config.get('page_recognition').get('start')))

    subproject_start_format_path = os.path.abspath(
        os.path.join(subproject_path, config.get('format')))
    mkpath(subproject_start_format_path)

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

    # получить список pdf файлов в папке pdf
    if filepath is not False:
        fso_start_pdf = [filepath]
    else:
        fso_start_pdf = scan_dir_os(subproject_start_pdf_path)

    dpi = config.get('dpi')

    files_to_convert_to_black_and_white = []

    # сконвертировать pdf файлы в png или jpg из папки scan см. config.get('format')
    for f in fso_start_pdf:
        rewrite = False
        if os.path.splitext(f)[0].endswith('b'):
            rewrite = True
            save_format = os.path.abspath(os.path.join(subproject_start_format_path, os.path.basename(
                os.path.splitext(f)[0][:-1]) + '.' + config.get('format')))
            files_to_convert_to_black_and_white.append(save_format)
        else:
            save_format = os.path.abspath(os.path.join(subproject_start_format_path, os.path.basename(
                os.path.splitext(f)[0]) + '.' + config.get('format')))

        if not os.path.exists(save_format) or rewrite:
            page = convert_from_path(f, dpi)

        if not os.path.exists(save_format) or rewrite:
            if config.get('format') == 'jpg':
                page[0].save(save_format, 'JPEG')

            if config.get('format') == 'png':
                page[0].save(save_format, 'PNG')

            print(f, '=>', save_format)

    ret_values = []

    # получить список png или jpg файлов в папке png или jpg см. config.get('format')
    if filepath is not False:
        fso_start_format = [save_format]
        ret_values.append(save_format)
    else:
        fso_start_format = scan_dir_os(subproject_start_format_path)

    height = 800
    width = 800
    blank_img = np.zeros((height, width, 3), np.uint8)

    # получить из отсканированных изображений обработанные и сохранить в результирующую папку
    i = 0
    for f in fso_start_format:
        fname = os.path.split(f)[-1]
        fn = os.path.splitext(fname)[0]
        ext = os.path.splitext(fname)[-1]
        dig = get_cnt_num_from_string(str_to_int(fn))
        if not dig:
            raise RuntimeError(f'Цифры не найдены в имени файла {f}')

        debug = False

        # определить имя файла, исключая расширение
        src_name = os.path.basename(f).split('.')[0]

        # определить количество разрядов в имени источника
        dig = get_cnt_num_from_string(src_name)

        # прочитать файл изображения
        src_image = cv.imread(f)

        # получить список картинок
        img_list = get_result_images(src_image, debug)

        if not img_list:
            #raise RuntimeError(f'Картинки не обработались в файле {filename}')
            print(f'Картинки не обработались в файле {f}')
            # картинка пустышка
            img = blank_img
            result_name = get_result_name(subproject_result_main_format_path, dig)
            result_filename = f'{result_name}{ext}'
            result_path_ = os.path.join(subproject_result_main_format_path, result_filename)
            cv.imwrite(result_path_, img)
            print(i, f, '=>', result_path_)
            ret_values.append(result_path_)

            i += 1
        else:
            if len(img_list) == 2:
                h1, w1 = img_list[0].shape[:2]
                h2, w2 = img_list[1].shape[:2]

                s1 = h1 * w1 / 1000
                s2 = h2 * w2 / 1000

                if s1 > s2:
                    diff_perc = 100 - (s2 * 100 / s1)
                    if diff_perc > 15:
                        img1 = img_list[0][0:h1, 0:floor(w1/2)]
                        img2 = img_list[0][0:h1, floor(w1/2):w1]
                        img_list[0] = img1
                        img_list[1] = img2
                elif s1 < s2:
                    diff_perc = 100 - (s1 * 100 / s2)
                    if diff_perc > 15:
                        img1 = img_list[1][0:h2, 0:floor(w2/2)]
                        img2 = img_list[1][0:h2, floor(w2/2):w2]
                        img_list[0] = img1
                        img_list[1] = img2

                h1, w1 = img_list[0].shape[:2]
                h2, w2 = img_list[1].shape[:2]

                margin1 = floor(w1 * 0.1)
                margin2 = floor(w2 * 0.1)

                img1 = img_list[0][0:h1, margin1:w1]
                img2 = img_list[1][0:h2, 0:w2-margin2]

                img_list[0] = img1
                img_list[1] = img2

            for img in img_list:
                result_name = get_result_name(subproject_result_main_format_path, dig)
                result_filename = f'{result_name}{ext}'
                result_path_ = os.path.join(subproject_result_main_format_path, result_filename)
                #showimg(img)
                cv.imwrite(result_path_, img)
                print(i, f, '=>', result_path_)
                ret_values.append(result_path_)

                i += 1

    return ret_values


def showimg(img):
    cv.namedWindow("test", cv.WINDOW_NORMAL)
    img = np.array(img,dtype=float)/float(255)
    h, w = img.shape[:2]
    r = w / h
    wh = 1000
    ww = floor(r * wh)
    cv.imshow('test',img)
    cv.resizeWindow('test',ww,wh)
    cv.waitKey(0)
