#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum(lst[0] * lst[1] for lst in my_list) \
        / sum(map(lambda x: x[1], my_list))
