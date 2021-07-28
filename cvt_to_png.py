#!/usr/bin/env python3
""""Программа преобразования из pdf в png"""


import sys
from pdf2image import convert_from_path


def _help():
    print(str(sys.argv[0]) + " input file " + " output file ")

def main():
    """"Главная функция"""

    if len(sys.argv) == 3:
        inf = sys.argv[1]
        outf = sys.argv[2]

        pages = convert_from_path(inf, 100)

        pages[0].save(outf, 'PNG')
    else:
        _help()


if __name__ == "__main__":
    main()
