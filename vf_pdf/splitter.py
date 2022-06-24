#!/usr/bin/env python3
"""Файл разделения pdf на страницы"""


import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

sys.path.append("..")
from vf_base.digits import digits


def splitter(filepath, output_path):
    r = PdfFileReader(filepath)

    num_all_pages = r.getNumPages()
    dig = digits(num_all_pages)
    file_size = os.path.getsize(filepath)
    dig_file_size = digits(file_size)

    for page in range(num_all_pages):
        w = PdfFileWriter()
        w.addPage(r.getPage(page))

        pdf_output_filename = os.path.join(output_path, '{:{fill}{align}{width}}.pdf'.format(
            page+1, fill=0, align='>', width=dig))

        with open(pdf_output_filename, 'wb') as out:
            w.write(out)
            pdffsize = os.path.getsize(pdf_output_filename)
            print('Создан: {}'.format(pdf_output_filename) +
                  ' Размер: {:{fill}{align}{width}}'.format(pdffsize, fill=0, align='>', width=dig_file_size))
