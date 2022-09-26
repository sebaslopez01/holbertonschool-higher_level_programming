#!/usr/bin/python3


def best_score(a_dictionary: dict):
    try:
        max_score = max(a_dictionary.values())
    except ValueError:
        return None
    result = next(filter(lambda x: x[1] == max_score, a_dictionary.items()))[0]

    return result
