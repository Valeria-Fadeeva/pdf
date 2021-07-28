#!/usr/bin/env python3
"""Файл слияния pdf"""


from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def merger(flist, output_path):
    """Функция слияния pdf"""
    w = PdfFileWriter()
    for fname in flist:
        fname = str(fname)
        r = PdfFileReader(fname)
        print('Читаем ' + fname)

        for page in range(r.getNumPages()):
            w.addPage(r.getPage(page))

    with open(output_path, 'wb') as fh:
        print('Записываем ' + output_path)
        w.write(fh)


def merger2(flist, output_path):
    """Функция слияния pdf"""
    m = PdfFileMerger()

    for fname in flist:
        m.append(fname)
        #m.append(PdfFileReader(open(fname, 'rb')))
        print('Добавляем ' + str(fname))

    with open(output_path, 'wb') as fh:
        print('Записываем ' + str(output_path))
        m.write(fh)
