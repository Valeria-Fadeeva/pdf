#!/usr/bin/env python3
""""Программа преобразования из png, jpg в pdf"""


import sys
import img2pdf


def _help():
    print(str(sys.argv[0]) + " input file " + " output file ")

def main():
    """"Главная функция"""

    if len(sys.argv) == 3:
        inf = sys.argv[1]
        outf = sys.argv[2]

        with open(outf, "wb") as f:
            f.write(img2pdf.convert(inf))
            f.close()
    else:
        _help()


if __name__ == "__main__":
    main()
