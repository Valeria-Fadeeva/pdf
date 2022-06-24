#!/usr/bin/env python3
"""Файл функций обработки изображения"""


import numpy as np
import cv2 as cv


def gray(image):
    """Функция получения серого изображения"""

    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return image


def threshold(image, start=150, end=255):
    """Функция получения черно-белого изображения"""

    image = cv.threshold(image, start, end, cv.THRESH_BINARY)[1]
    return image


def threshold_invert(image, start=150, end=255):
    """Функция получения инвертированного черно-белого изображения"""

    image = cv.threshold(image, start, end, cv.THRESH_BINARY_INV)[1]
    return image


def invert(image):
    """Функция инвертирования цветов изображения"""

    image = cv.bitwise_not(image)
    return image


def erosion(image, kernel):
    """Функция эрозии изображения"""

    image = cv.erode(image, kernel, iterations=10)
    return image


def dilate(image, kernel):
    """Функция расширения изображения"""

    image = cv.dilate(image, kernel, iterations=10)
    return image


def blur(image):
    """Функция размытия изображения"""

    image = cv.medianBlur(image, 9)
    return image


def gaussian_blur(image):
    """Функция размытия изображения по Гаусу"""

    image = cv.GaussianBlur(image, (3, 3), 0)
    return image


def floodfill(image):
    """Функция заполнения изображения"""

    im_th = cv.threshold(image, 220, 255, cv.THRESH_BINARY_INV)[1]
    im_floodfill = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(im_floodfill, mask, (0, 0), 255)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    image = im_th | im_floodfill_inv
    return image


def canny(image):
    """Функция нахождения границ изображения по Кэнни"""

    image = cv.Canny(image, 10, 250)
    return image


def closed(image, kernel):
    """Функция закрытия границ изображения"""

    image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    return image


def image_prepare(image, start=150, end=255, debug=False):
    """Функция подготовки изображения"""

    kernel = np.ones((3, 3), np.uint8)
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))

    if (len(image.shape) < 3):
        image = gray(image)
    elif len(image.shape) == 3:
        # смена цветовой модели с BGR на GRAY scale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        raise RuntimeError('Странное цветовое пространство')

    if debug is True:
        n = 0
        rf = f'lap/{n}_gray.png'
        cv.imwrite(rf, image)

    image = threshold(image, start, end)
    if debug is True:
        n += 1
        rf = f'lap/{n}_threshold.png'
        cv.imwrite(rf, image)

    image = erosion(image, kernel2)
    if debug is True:
        n += 1
        rf = f'lap/{n}_erosion.png'
        cv.imwrite(rf, image)

    image = invert(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_invert.png'
        cv.imwrite(rf, image)

    image = dilate(image, kernel)
    if debug is True:
        n += 1
        rf = f'lap/{n}_dilate.png'
        cv.imwrite(rf, image)

    image = blur(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_blur.png'
        cv.imwrite(rf, image)

    image = floodfill(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_floodfill.png'
        cv.imwrite(rf, image)

    '''
    image = threshold_invert(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_threshold_invert.png'
        cv.imwrite(rf, image)
    '''

    image = canny(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_canny.png'
        cv.imwrite(rf, image)

    image = closed(image, kernel2)
    if debug is True:
        n += 1
        rf = f'lap/{n}_closed.png'
        cv.imwrite(rf, image)

    return image


def image_prepare_alt(image, start=150, end=255, debug=False):
    """Функция подготовки изображения (альтернативная)"""

    if (len(image.shape) < 3):
        image = gray(image)
    elif len(image.shape) == 3:
        # смена цветовой модели с BGR на GRAY scale
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    else:
        raise RuntimeError('Странное цветовое пространство')
    if debug is True:
        n = 0
        rf = f'lap/{n}_alt_gray.png'
        cv.imwrite(rf, image)

    # уменьшение резкости
    image = gaussian_blur(image)
    if debug is True:
        n += 1
        rf = f'lap/{n}_alt_gaussian_blur.png'
        cv.imwrite(rf, image)

    # создание черно-белого изображения
    # image = cv.threshold(image, 150, 255, cv.THRESH_BINARY)[1]
    image = cv.threshold(image, start, end, cv.THRESH_BINARY)[1]
    if debug is True:
        n += 1
        rf = f'lap/{n}_alt_threshold.png'
        cv.imwrite(rf, image)

    return image
