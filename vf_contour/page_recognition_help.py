#!/usr/bin/env python3
"""Справка по использованию программы page_recognition"""


import os
import sys


def page_recognition_help():
    """Функция справки по использованию программы page_recognition"""

    args_len = len(sys.argv)

    if args_len == 1:
        col1 = 15
        col2 = 25
        col3 = 40
        max_width = 80
        p = os.path.split(sys.argv[0])[-1]

        print('Использование:')
        print('{:{fill}{align}{width}}'.format(
            '', fill='=', align='^', width=max_width))
        print(
            '{0:{fill}{align}{width}}'.format('программа', fill=' ', align='<', width=col1-1) + '|' +
            '{0:{fill}{align}{width}}'.format('аргумент', fill=' ', align='<', width=col2-1) + '|' +
            '{0:{fill}{align}{width}}'.format(
                'подсказка', fill=' ', align='<', width=col3)
        )
        print('{:{fill}{align}{width}}'.format(
            '', fill='=', align='^', width=max_width))
        print(
            '{0:{fill}{align}{width}}'.format(p, fill=' ', align='<', width=col1) +
            '{0:{fill}{align}{width}}'.format('"путь к pdf-проекту"', fill=' ', align='<', width=col2) +
            '{0:{fill}{align}{width}}'.format(
                'Пустота =)', fill=' ', align='<', width=col3)
        )
        print()
        print(
            '{0:{fill}{align}{width}}'.format(p, fill=' ', align='<', width=col1) +
            '{0:{fill}{align}{width}}'.format('-l', fill=' ', align='<', width=col2) +
            '{0:{fill}{align}{width}}'.format(
                'Вывести список подпроектов в каталоге scan', fill=' ', align='<', width=col3)
        )
        exit(0)
