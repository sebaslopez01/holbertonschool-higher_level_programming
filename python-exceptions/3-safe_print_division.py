#!/usr/bin/python3


def safe_print_division(a: int, b: int):
    result = 0

    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print('Inside result: {}'.format(result))

    return result
