#!/usr/bin/env python3
"""Программа распознавания контуров страниц и сохранения их в png или jpg"""


import os
import sys
import ast
#import argparse
from vf_base.config import Config
from vf_base.check_file import check_file
from vf_contour.page_recognition_help import page_recognition_help
from vf_contour.page_recognition import page_recognition


with open('config.cfg', 'r', encoding='utf-8') as file:
    s = file.read().replace('\r\n', '')
    s = s.replace('\n', '')
    s = s.replace(' ', '')

    d = ast.literal_eval(s)

    config = Config(d)


def main():
    """Главная функция"""

    args_len = len(sys.argv)
    check_file_var = False
    filepath = False

    project = os.path.abspath(
        os.path.join(
            config.get('project'),
            config.get('scan')
        )
    )

    page_recognition_help()

    if args_len == 2:
        if sys.argv[1] == '-l':
            print('Список подпроектов в каталоге scan: ')
            for i in os.listdir(path=project):
                if os.path.isdir(os.path.abspath(os.path.join(project, i))):
                    print(i)
        else:
            filepath = sys.argv[1]
            filepath = filepath.strip()
            check_file_var = check_file(filepath)
            print(filepath)
            print('Производим поиски')
            if filepath is not False:
                temp_filepath = os.path.abspath(filepath)
                check_file_var = check_file(temp_filepath)
                if check_file_var is True:
                    filepath = temp_filepath
                else:
                    temp_filepath = os.path.abspath(
                        os.path.join(project, filepath))
                    check_file_var = check_file(temp_filepath)
                    if check_file_var is True:
                        filepath = temp_filepath

    if args_len > 2:
        print('Соединяем части параметров в одну строку')
        filepath = ' '.join(sys.argv)
        filepath = filepath.replace(sys.argv[0], '', 1)
        filepath = filepath.strip()
        print(filepath)
        print('Производим поиски')
        if filepath is not False:
            temp_filepath = os.path.abspath(filepath)
            check_file_var = check_file(temp_filepath)
            if check_file_var is True:
                filepath = temp_filepath
            else:
                temp_filepath = os.path.abspath(
                    os.path.join(project, filepath))
                check_file_var = check_file(temp_filepath)
                if check_file_var is True:
                    filepath = temp_filepath

    if check_file_var is True:
        subproject = os.path.basename(filepath)
        page_recognition(subproject, config)
    else:
        if 'temp_filepath' in locals():
            print(f'Не найден {temp_filepath}')
        exit()

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description="Programm: finding the outline of an object and cropping", epilog='Use %(prog)s {command} -h to get help on individual commands')
    #parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + vf_pdf.copyright)
    #args = parser.parse_args()
    main()
