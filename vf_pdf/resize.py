#!/usr/bin/env python3
"""Файл изменения размеров изображения"""


import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image


def resize(filename, max_width):
    """Функция изменения размеров изображения"""
    if os.path.exists(filename) :
        if os.path.getsize(filename) > 0:
            if os.path.splitext(filename)[1] == '.pdf':
                r = PdfFileReader(filename)

                # Getting only first page!
                page = r.getPage(0)

                # size in pt
                width = float(page.mediaBox.getWidth())
                height = float(page.mediaBox.getHeight())
                aspect_ratio = float(height/width)

                pt = 1/72*100

                width_px = int(round(width * pt, 0))
                height_px = int(round(height * pt, 0))

                if width_px != max_width:
                    new_width_px = max_width
                    new_height_px = new_width_px * aspect_ratio
                    new_height_px = int(round(new_height_px, 0))

                    new_width = int(round(new_width_px / pt, 0))
                    new_height = int(round(new_height_px / pt, 0))

                    page.scaleTo(new_width, new_height)

                    w = PdfFileWriter()
                    w.addPage(page)

                    with open(filename, "wb") as outfp:
                        w.write(outfp)

            if os.path.splitext(filename)[1] == '.png' or os.path.splitext(filename)[1] == '.jpg':
                im = Image.open(filename, mode="r")

                width_px, height_px = im.size

                if width_px != max_width:
                    aspect_ratio = float(height_px/width_px)

                    new_width_px = max_width
                    new_height_px = new_width_px * aspect_ratio
                    new_height_px = int(round(new_height_px, 0))

                    newsize = (new_width_px, new_height_px)
                    im = im.resize(newsize)

                    im = im.save(filename)
        else:
            print(filename + ' has zero size')
    else:
        print(filename + ' does not exist')
