#!/usr/bin/env python3
"""Программа соединения файлов в многостраничный pdf"""


import os
import sys
import ast
from vf_base.config import Config
from vf_base.check_file import check_file
from vf_pdf.merge_help import merge_help
from vf_pdf.merge import merge


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
            config.get('split')
        )
    )

    merge_help()

    if args_len == 2:
        if sys.argv[1] == '-l':
            print('Список подпроектов в каталоге split: ')
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
                    temp_filepath = os.path.abspath(os.path.join(project, filepath))
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
                temp_filepath = os.path.abspath(os.path.join(project, filepath))
                check_file_var = check_file(temp_filepath)
                if check_file_var is True:
                    filepath = temp_filepath

    if check_file_var is True:
        subproject = os.path.basename(filepath)
        merge(subproject, config)
    else:
        exit()

if __name__ == '__main__':
    main()
