#!/usr/bin/python3


def list_division(my_list_1: list, my_list_2: list, list_length: int):
    new_list = []

    try:
        for i in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[i]
            except TypeError:
                print('wrong type')
            except ZeroDivisionError:
                print('division by 0')
            finally:
                new_list.append(result)
    except IndexError:
        print('out of range')

    return new_list
