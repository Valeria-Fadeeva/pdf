#!/usr/bin/env python3
"""Программа распознавания контуров страниц и сохранения их в png или jpg"""


import os
import sys
import ast
import subprocess
from pynput import keyboard
from vf_base.config import Config
from vf_base.check_file import check_file
from vf_contour.per_page_recognition_help import per_page_recognition_help
from vf_contour.page_recognition import page_recognition
from vf_base.scan_dir_os import scan_files_os

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
    scan = False

    project = os.path.abspath(
        os.path.join(
            config.get('project'),
            config.get('scan')
        )
    )

    per_page_recognition_help()

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
        filepath = ' '.join(sys.argv)
        if sys.argv[1] == '-s':
            scan = True
            filepath = filepath.replace(sys.argv[0], '', 1)
            filepath = filepath.replace(sys.argv[1], '', 1)
        else:
            filepath = filepath.replace(sys.argv[0], '', 1)

        filepath = filepath.strip()

        print(f'Производим поиски {filepath}')
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
        print('Работаем')
        print(filepath)
        subproject_path_pdf = os.path.dirname(filepath)
        subproject_path = os.path.dirname(subproject_path_pdf)
        subproject = os.path.basename(subproject_path)

        ret_values = page_recognition(subproject, config, filepath)
        ret_values.insert(0, 'viewer')
        subprocess.run(ret_values, shell=True, check=True)

        arr_files = scan_files_os(subproject_path_pdf)

        while scan is False:
            print('Для продолжения нажмите Enter или пробел')
            print('Для выхода нажмите ESC')
            with keyboard.Events() as events:
                # Block for as much as possible
                event = events.get(1e6)

                if event.key == keyboard.Key.space or event.key == keyboard.Key.enter:
                    index = arr_files.index(filepath)
                    filepath = arr_files[index+1]
                    print(filepath)
                    ret_values = page_recognition(subproject, config, filepath)
                    ret_values.insert(0, 'viewer')
                    subprocess.run(ret_values, shell=True, check=True)

                if event.key == keyboard.Key.esc:
                    print("ESC")
                    break
    else:
        if 'temp_filepath' in locals():
            print(f'Не найден {temp_filepath}')
        exit()


if __name__ == '__main__':
    main()
