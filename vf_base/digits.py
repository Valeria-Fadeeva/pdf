#!/usr/bin/env python3


def digits(n):
    """Функция определение разрядности числа"""

    n = int(n)
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i


def str_to_int(s: str):
    """Функция сохранения нулей в строке"""

    n = None
    for i in s:
        if i.isnumeric():
            if n is None:
                n = str(i)
            elif n is not None:
                n += str(i)

    return n


def get_cnt_num_from_string(s: str):
    """Функция получения количества чисел в строке"""

    n = 0
    for i in s:
        if i.isnumeric():
            n += 1

    return n


def dict_int_range_search(d: dict, start: int, end: int) -> tuple | None:
    """Функция поиска числа в словаре из заданного диапазона"""

    k: list = []
    v: list = []

    for i in range(start, end):
        if d.get(i) is None:
            pass
        else:
            k.append(i)
            v.append(d.get(i))

    if len(v) > 0:
        return k, v
    else:
        return None
