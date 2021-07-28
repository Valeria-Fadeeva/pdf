#!/usr/bin/env python3
"""Конфигурация"""


class MetaSingleton(type):
    """Метакласс синглтона"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=MetaSingleton):
    """Класс конфигурации"""

    #def __init__(self, *args, **kwargs):
    def __init__(self, *args, **kwargs):
        """Инициализация класса

        args is a tuple
        args[0] want to be a dict

        kwargs is a dict

        Returns:
            [dict]: [object saved configure variables]
        """

        if isinstance(args[0], dict):
            self.args = args[0]
        else:
            self.args = {}

    def get(self, key):
        """Функция получения значения"""
        return self.args.get(key)

    def set(self, key, value):
        """Функция присвоения значения"""
        return self.args.update({key: value})

    def keys(self):
        """Функция получения ключей"""
        return self.args.keys()

    def items(self):
        """Функция получения элементов"""
        return self.args.items()
