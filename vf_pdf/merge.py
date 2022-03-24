#!/usr/bin/env python3
"""Главный файл модуля merge"""


import os
import sys
from pdf2image import convert_from_path
from PIL import Image
import cv2 as cv

from .image_convert_to_black_and_white import image_convert_to_black_and_white
from .merger import merger

sys.path.append("..")
from vf_base.mkpath import mkpath
from vf_base.scan_dir_os import scan_dir_os
from vf_base.digits import digits


def merge(subproject, config):
    """Главная функция модуля merge"""

    # subproject dir
    subproject_path = os.path.abspath(os.path.join(
        config.get('project'), config.get('split'), subproject))
    mkpath(subproject_path)
    print(f"mkpath(subproject_path) {subproject_path}")

    # start dirs
    subproject_start_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('start')))

    subproject_start_pdf_path = os.path.abspath(
        os.path.join(subproject_start_path, 'pdf'))
    mkpath(subproject_start_pdf_path)
    print(f"mkpath(subproject_start_pdf_path) {subproject_start_pdf_path}")

    subproject_start_format_path = os.path.abspath(
        os.path.join(subproject_start_path, config.get('format')))
    mkpath(subproject_start_format_path)
    print(f"mkpath(subproject_start_format_path) {subproject_start_format_path}")

    #subproject_start_format_convert_path = os.path.join(subproject_start_path, 'convert')
    # mkpath(subproject_start_format_convert_path)

    # scan dirs
    subproject_scan_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('scan')))

    subproject_scan_pdf_path = os.path.abspath(
        os.path.join(subproject_scan_path, 'pdf'))
    mkpath(subproject_scan_pdf_path)
    print(f"mkpath(subproject_scan_pdf_path) {subproject_scan_pdf_path}")

    subproject_scan_format_path = os.path.abspath(
        os.path.join(subproject_scan_path, config.get('format')))
    mkpath(subproject_scan_format_path)
    print(f"mkpath(subproject_scan_format_path) {subproject_scan_format_path}")

    #subproject_scan_format_convert_path = os.path.join(subproject_scan_path, 'convert')
    # mkpath(subproject_scan_format_convert_path)

    # main dirs
    subproject_main_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('main')))

    subproject_main_pdf_path = os.path.abspath(
        os.path.join(subproject_main_path, 'pdf'))
    mkpath(subproject_main_pdf_path)
    print(f"mkpath(subproject_main_pdf_path) {subproject_main_pdf_path}")

    subproject_main_format_path = os.path.abspath(
        os.path.join(subproject_main_path, config.get('format')))
    mkpath(subproject_main_format_path)
    print(f"mkpath(subproject_main_format_path) {subproject_main_format_path}")

    #subproject_main_format_convert_path = os.path.join(subproject_main_path, 'convert')
    # mkpath(subproject_main_format_convert_path)

    # result dir
    result_path = os.path.abspath(os.path.join(
        subproject_path, config.get('result')))
    mkpath(result_path)
    print(f"mkpath(result_path) {result_path}")

    subproject_result_pdf_path = os.path.abspath(
        os.path.join(result_path, 'pdf'))
    mkpath(subproject_result_pdf_path)
    print(f"mkpath(subproject_result_pdf_path) {subproject_result_pdf_path}")

    subproject_result_format_path = os.path.abspath(
        os.path.join(result_path, config.get('format')))
    mkpath(subproject_result_format_path)
    print(f"mkpath(subproject_result_format_path) {subproject_result_format_path}")

    # получить список pdf файлов в папке start, scan и main
    fso_start_pdf = scan_dir_os(subproject_start_pdf_path)
    fso_scan_pdf = scan_dir_os(subproject_scan_pdf_path)
    fso_main_pdf = scan_dir_os(subproject_main_pdf_path)

    dpi = config.get('dpi')

    files_to_convert_to_black_and_white = []

    # сконвертировать pdf файлы в png или jpg в папке start см. config.get('format')
    for f in fso_start_pdf:
        rewrite = False
        if os.path.splitext(f)[0].endswith('b'):
            rewrite = True
            save_format = os.path.join(subproject_start_format_path, os.path.basename(
                os.path.splitext(f)[0][:-1]) + '.' + config.get('format'))
            files_to_convert_to_black_and_white.append(save_format)
        else:
            save_format = os.path.join(subproject_start_format_path, os.path.basename(
                os.path.splitext(f)[0]) + '.' + config.get('format'))

        if not os.path.exists(save_format) or rewrite:
            page = convert_from_path(f, dpi)

        if not os.path.exists(save_format) or rewrite:
            if config.get('format') == 'jpg':
                page[0].save(save_format, 'JPEG')

            if config.get('format') == 'png':
                page[0].save(save_format, 'PNG')

            print(f, '=>', save_format)

    # сконвертировать pdf файлы в png или jpg в папке scan см. config.get('format')
    for f in fso_scan_pdf:
        rewrite = False
        if os.path.splitext(f)[0].endswith('b'):
            rewrite = True
            save_format = os.path.join(subproject_scan_format_path, os.path.basename(
                os.path.splitext(f)[0][:-1]) + '.' + config.get('format'))
            files_to_convert_to_black_and_white.append(save_format)
        else:
            save_format = os.path.join(subproject_scan_format_path, os.path.basename(
                os.path.splitext(f)[0]) + '.' + config.get('format'))

        if not os.path.exists(save_format) or rewrite:
            page = convert_from_path(f, dpi)

        if not os.path.exists(save_format) or rewrite:
            if config.get('format') == 'jpg':
                page[0].save(save_format, 'JPEG')

            if config.get('format') == 'png':
                page[0].save(save_format, 'PNG')

            print(f, '=>', save_format)

    # сконвертировать pdf файлы в png или jpg в папке main см. config.get('format')
    for f in fso_main_pdf:
        rewrite = False
        if os.path.splitext(f)[0].endswith('b'):
            rewrite = True
            save_format = os.path.join(subproject_main_format_path, os.path.basename(
                os.path.splitext(f)[0][:-1]) + '.' + config.get('format'))
            files_to_convert_to_black_and_white.append(save_format)
        else:
            save_format = os.path.join(subproject_main_format_path, os.path.basename(
                os.path.splitext(f)[0]) + '.' + config.get('format'))

        if not os.path.exists(save_format) or rewrite:
            page = convert_from_path(f, dpi)

        if not os.path.exists(save_format) or rewrite:
            if config.get('format') == 'jpg':
                page[0].save(save_format, 'JPEG')

            if config.get('format') == 'png':
                page[0].save(save_format, 'PNG')

            print(f, '=>', save_format)

    # получить список png или jpg файлов в папках start, scan, main
    fso_start_format = scan_dir_os(subproject_start_format_path)
    fso_scan_format = scan_dir_os(subproject_scan_format_path)
    fso_main_format = scan_dir_os(subproject_main_format_path)

    # словарь со списком png или jpg файлов в папке start, ключами являются имена файлов
    dict_fso_scan_format = {}
    for f in fso_scan_format:
        k = os.path.split(f)[-1]
        v = f
        dict_fso_scan_format.update({k: v})

    # словарь со списком png или jpg файлов в папке main, ключами являются имена файлов
    dict_fso_main_format = {}
    for f in fso_main_format:
        k = os.path.split(f)[-1]
        v = f
        dict_fso_main_format.update({k: v})

    # обновить словать, заменив в нем элементы c одинаковым ключом и добавив новые элементы
    # папка main по сути является неизменяемой, в ней вручную удаляются лишние файлы
    dict_fso_main_format.update(dict_fso_scan_format)

    fso_all_format = [*fso_start_format, *dict_fso_main_format.values()]
    if len(fso_all_format) == 0:
        err = 'Пустой список \n' + 'subproject_path = ' + \
            str(subproject_path) + '\nsubproject = ' + str(subproject)
        raise Exception(err)

    max_width = False
    min_width = False

    # словарь с размерами картинок, ключами являются пути к файлам
    f_all = {}

    # прочитать файлы, вычислить максимальную и минимальную ширину
    for f in fso_all_format:
        im = Image.open(f, mode='r')
        im = im.convert('RGB')

        width_px, height_px = im.size

        if max_width is False:
            max_width = width_px

        if max_width < width_px:
            max_width = width_px

        if min_width is False:
            min_width = width_px

        if min_width > width_px:
            min_width = width_px

        # Определить ориентацию страницы
        orient = width_px / height_px
        if orient < 1:
            orient_text = 'v'
        else:
            orient_text = 'h'

        f_all.update({f: (width_px, height_px, orient_text)})

    top_min = min(min_width, config.get('max_width_px'))

    # изменить размеры страницы, конвертировать в Ч/Б если нужно
    l = len(fso_all_format)
    dig = digits(l)

    i = 0
    for f in fso_all_format:
        saved = False
        fname = '{:{fill}{align}{width}}.'.format(
            i, fill=0, align='>', width=dig) + config.get('format')
        format_output_filename = os.path.join(
            subproject_result_format_path, fname)

        if os.path.exists(format_output_filename):
            saved = True

        if saved is False:
            width_px, height_px, orient_text = f_all.get(f)

            if orient_text == 'v':
                t_min = top_min
            elif orient_text == 'h':
                t_min = top_min * 1.54

            if width_px > t_min:
                if f not in files_to_convert_to_black_and_white:
                    im = Image.open(f, mode='r')
                    im = im.convert('RGB')

                    aspect_ratio = float(height_px/width_px)

                    new_width_px = int(round(t_min, 0))
                    new_height_px = new_width_px * aspect_ratio
                    new_height_px = int(round(new_height_px, 0))

                    newsize = (new_width_px, new_height_px)
                    im = im.resize(size=newsize, resample=Image.LANCZOS)
                    im = im.save(format_output_filename,
                                 compress_level=0, quality=100, optimize=False)
                    saved = True
                    print('Изменён размер страницы', height_px,
                          width_px, '=>', new_width_px, new_height_px)
                    print(f, '=>', format_output_filename)

                if f in files_to_convert_to_black_and_white:
                    original_image = cv.imread(f)

                    aspect_ratio = float(height_px/width_px)

                    new_width_px = t_min
                    new_height_px = new_width_px * aspect_ratio
                    new_height_px = int(round(new_height_px, 0))

                    newsize = (new_width_px, new_height_px)
                    original_resized_image = cv.resize(
                        original_image, dsize=newsize, interpolation=cv.INTER_LANCZOS4)

                    cv.imwrite(format_output_filename, original_resized_image)
                    saved = True
                    print('Конвертация в Ч/Б, изменён размер страницы',
                          height_px, width_px, '=>', new_width_px, new_height_px)
                    print(f, '=>', format_output_filename)

            if f in files_to_convert_to_black_and_white:
                image_convert_to_black_and_white(
                    format_output_filename, config.get('blur_variant'))
                #test_image_convert_to_black_and_white(format_output_filename, config, subproject)
                saved = True
                print('Удаление пятен, размытие')
                print(format_output_filename)

            if saved is False:
                if not os.path.exists(format_output_filename):
                    with Image.open(f) as im:
                        im = im.convert('RGB')
                        im.save(format_output_filename, compress_level=0,
                                quality=100, optimize=False)
                        print('Сохранено без конвертации и изменения размеров')
                        print(f, '=>', format_output_filename)
        i += 1

    fso_all_format = scan_dir_os(subproject_result_format_path)
    l = len(fso_all_format)
    dig = digits(l)

    for i in range(l):
        fname = '{:{fill}{align}{width}}.pdf'.format(
            i, fill=0, align='>', width=dig)
        pdf_output_filename = os.path.join(subproject_result_pdf_path, fname)

        if not os.path.exists(pdf_output_filename):
            with Image.open(fso_all_format[i]) as im:
                im = im.convert('RGB')
                im.save(pdf_output_filename, format='PDF',
                        resoultion=float(dpi), quality=100, optimize=False)
                print(i, fname, pdf_output_filename, 'сохранён как pdf')
        else:
            print(i, fname, pdf_output_filename, 'существует')

    rp = subproject_result_pdf_path
    pdf_list = [os.path.abspath(os.path.join(rp, x)) for x in os.listdir(rp)]

    # r dir
    r_path = os.path.join(config.get('project'), config.get('result'))
    mkpath(r_path)
    print(f"mkpath(r_path) {r_path}")

    result_output_filename = os.path.abspath(
        os.path.join(r_path, subproject + '.pdf'))

    merger(pdf_list, result_output_filename)

    exit()
