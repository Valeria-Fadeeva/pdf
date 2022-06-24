#!/usr/bin/env python3
"""Файл функции получения контура"""


import cv2 as cv
from imutils import grab_contours


def get_contours(image, mode: int = 2) -> list:
    """Функция получения контура"""

    # cv.RETR_LIST       → Retrieve all contours
    # cv.RETR_EXTERNAL   → Retrieves external or outer contours only
    # cv.RETR_CCOMP      → Retrieves all in a 2-level hierarchy
    # cv.RETR_TREE       → Retrieves all in the full hierarchy

    if mode == 1:
        contour_type = cv.RETR_LIST
    elif mode == 2:
        contour_type = cv.RETR_EXTERNAL
    elif mode == 3:
        contour_type = cv.RETR_CCOMP
    elif mode == 4:
        contour_type = cv.RETR_TREE
    else:
        contour_type = cv.RETR_EXTERNAL

    # нахождение контуров в изображении и подсчет количества
    contours = cv.findContours(image, contour_type, cv.CHAIN_APPROX_SIMPLE)

    contours = grab_contours(contours)

    return contours
