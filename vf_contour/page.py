#!/usr/bin/env python3
"""Файл функций получения частей изображения по контурам"""


from math import floor
import numpy as np
import cv2 as cv
from imutils import perspective
from .vertex_quadrangle_v2 import get_quadrangle_vertices


def page_process(image, contours, debug=False):
    """Функция получения частей изображения по контурам"""

    image_dict = {}
    # цикл по контурам
    for c in contours:
        # аппроксимация (сглаживание) контура
        perimetr = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.02 * perimetr, True)

        image_h, image_w = image.shape[:2]
        x, y, w, h = cv.boundingRect(approx)

        # если объект занимает больше 30% от ширины и высоты изображения
        if w >= (image_w * 0.3) and h >= (image_h * 0.1):
            #print('APPROX', len(approx))

            font = cv.FONT_HERSHEY_SIMPLEX

            if len(approx) >= 4:
                arr = []
                for g in approx:
                    lp_ = g.tolist()[0]
                    s_ = 'len {} {}'.format(len(approx), lp_)
                    #ps_ = '{}'.format(lp_)
                    #print(ps_, end=' ')
                    if debug is True:
                        #                        b, g, r
                        cv.circle(image, lp_, 10, (0, 0, 255), -1)
                        cv.putText(image, s_, lp_, font, 1,
                                (100, 127, 255), 2, cv.LINE_AA)

                    for hi in g:
                        arr.append([hi[0], hi[1]])

            rect = cv.minAreaRect(approx)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            pts = np.array(box)

            approx = get_quadrangle_vertices(arr, mode=2)
            if not isinstance(approx, np.ndarray) and not isinstance(approx, list) and len(approx) <= 1:
                raise RuntimeError('Вершины не получены')

            x = approx[0][0]
            y = approx[0][1]
            w = approx[2][0] - approx[0][0]
            h = approx[2][1] - approx[0][1]


            if debug is True:
                # выделение контуров
                #                                   b, g, r
                cv.drawContours(image, [approx], -1, (0, 255, 0), 4)

            if 'y' in locals() and 'x' in locals():
                crop_img = perspective.four_point_transform(image.copy(), pts)
                if not isinstance(crop_img, np.ndarray):
                    crop_img = image[y:y+h, x:x+w]

                image_dict[x] = crop_img
                print('[y:y+h, x:x+w]:', y, y+h, x, x+w, '\n\n')

    if debug is True:
        cv.imwrite('lap/result.png', image)

    ret_image_array = []
    i = 0
    if len(image_dict) == 1:
        img = image_dict[min(image_dict)]
        h, w = img.shape[:2]
        if w > h:
            crop_img1 = img[0:h, 0:round(w/2)]
            ret_image_array.append(crop_img1)

            if debug is True:
                rf = f'lap/result_crop_{i}.png'
                cv.imwrite(rf, crop_img1)

            crop_img2 = img[0:h, round(w/2):w]
            ret_image_array.append(crop_img2)

            if debug is True:
                i += 1
                rf = f'lap/result_crop_{i}.png'
                cv.imwrite(rf, crop_img2)
        else:
            ret_image_array.append(img)

            if debug is True:
                rf = f'lap/result_crop_{i}.png'
                cv.imwrite(rf, img)

    elif len(image_dict) == 2:
        image_dict = dict(sorted(image_dict.items()))

        for img in image_dict:
            ret_image_array.append(image_dict[img])

            if debug is True:
                rf = f'lap/result_crop_{i}.png'
                cv.imwrite(rf, image_dict[img])
                i += 1

    return ret_image_array
