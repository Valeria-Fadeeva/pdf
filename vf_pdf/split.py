#!/usr/bin/env python3
"""Главный файл модуля split"""


import os
import sys

from .splitter import splitter

sys.path.append("..")
from vf_base.mkpath import mkpath


def split(filepath, subproject, config):
    """Главная функция модуля split"""

    # subproject dir
    subproject_path = os.path.abspath(os.path.join(
        config.get('project'), config.get('split'), subproject))
    mkpath(subproject_path)

    # start dirs
    subproject_start_pdf_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('start'), 'pdf'))
    mkpath(subproject_start_pdf_path)

    subproject_start_format_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('start'), config.get('format')))
    mkpath(subproject_start_format_path)

    # scan dirs
    subproject_scan_pdf_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('scan'), 'pdf'))
    mkpath(subproject_scan_pdf_path)

    subproject_scan_format_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('scan'), config.get('format')))
    mkpath(subproject_scan_format_path)

    # main dirs
    subproject_main_pdf_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('main'), 'pdf'))
    mkpath(subproject_main_pdf_path)

    subproject_main_format_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('main'), config.get('format')))
    mkpath(subproject_main_format_path)

    # result dir
    result_path = os.path.abspath(os.path.join(
        subproject_path, config.get('subproject').get('main')))
    mkpath(result_path)

    splitter(filepath, subproject_main_pdf_path)

    exit()
