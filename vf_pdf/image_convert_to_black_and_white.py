#!/usr/bin/env python3
""""Преобразование из цветного изображения в черно-белое"""


import os
import sys
import cv2 as cv
sys.path.append("..")
from vf_base.mkpath import mkpath


def image_convert_to_black_and_white(filename, variant):
    """"Функция преобразования из цветного изображения в черно-белое"""

    #variants = ['0', '1', '2', '3', '1b', '2b', '3b', ]

    bw_image = False
    original_image = cv.imread(filename, 0)

    if variant == '3b':
        original_blur_image = cv.GaussianBlur(original_image, (1, 1), 0)
        bw_image = cv.threshold(original_blur_image, 0,
                                255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    elif variant == '2b':
        original_blur_image = cv.GaussianBlur(original_image, (1, 1), 0)
        bw_image = cv.adaptiveThreshold(
            original_blur_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    elif variant == '1b':
        original_blur_image = cv.blur(original_image, (3, 3))
        bw_image = cv.threshold(original_blur_image, 127,
                                255, cv.THRESH_BINARY)[1]
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    elif variant == '3':
        bw_image = cv.threshold(original_image, 0, 255,
                                cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    elif variant == '2':
        bw_image = cv.adaptiveThreshold(
            original_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    elif variant == '1':
        bw_image = cv.threshold(original_image, 127, 255, cv.THRESH_BINARY)[1]
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    else:
        bw_image = cv.threshold(original_image, 127, 255,
                                cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

    if bw_image is not False:
        cv.imwrite(filename, bw_image)


def test_image_convert_to_black_and_white(filename, config, subproject):
    """"Функция тестирования преобразования из цветного изображения в черно-белое"""

    test_path = os.path.join(config.get('project'), 'test', subproject)
    mkpath(test_path)
    print(f"mkpath(test_path) {test_path}")

    variants = ['0', '1', '2', '3', '1b', '2b', '3b', ]

    for variant in variants:
        bw_image = False
        original_image = cv.imread(filename, 0)

        if variant == '3b':
            original_blur_image = cv.GaussianBlur(original_image, (1, 1), 0)
            bw_image = cv.threshold(
                original_blur_image, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        elif variant == '2b':
            original_blur_image = cv.GaussianBlur(original_image, (1, 1), 0)
            bw_image = cv.adaptiveThreshold(
                original_blur_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        elif variant == '1b':
            #original_blur_image = cv.blur(original_image, (1, 1))
            #original_blur_image = cv.GaussianBlur(original_image, (1, 1), 0)
            original_blur_image = cv.bilateralFilter(original_image, 1, 2, 2)
            #thresh, bw_image = cv.threshold(original_blur_image, 127, 255, cv.THRESH_BINARY)
            bw_image = cv.threshold(
                original_blur_image, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        elif variant == '3':
            bw_image = cv.threshold(
                original_image, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        elif variant == '2':
            bw_image = cv.adaptiveThreshold(
                original_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        elif variant == '1':
            bw_image = cv.threshold(
                original_image, 127, 255, cv.THRESH_BINARY)[1]
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)
        else:
            bw_image = cv.threshold(
                original_image, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
            bw_image = cv.fastNlMeansDenoising(bw_image, h=50)

        if bw_image is not False:
            #cv.imwrite(filename, bw_image)

            p = os.path.join(test_path, str(variant))
            mkpath(p)
            print(f"mkpath(p) {p}")
            fp = os.path.join(p, os.path.basename(filename))
            print(fp)
            cv.imwrite(fp, bw_image)
