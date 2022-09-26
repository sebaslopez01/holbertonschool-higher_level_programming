#!/usr/bin/python3


def best_score(a_dictionary: dict):
    if a_dictionary is None:
        return None

    max_score = max(a_dictionary.values())
    result = next(filter(lambda x: x[1] == max_score, a_dictionary.items()))[0]

    return result
