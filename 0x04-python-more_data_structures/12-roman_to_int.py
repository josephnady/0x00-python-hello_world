#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    X = 10 / VII = 7  / IX = 9 /
    LXXXVII = 87 / DCCVII = 707 /XCIX = 99
    """
    roman_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not isinstance(roman_string, str):
        return 0

    for each in roman_string:
        if each not in list(roman_n.keys()):
            return 0

    res = [roman_n.get(i) for i in roman_string]
    i = 0
    res2 = []
    for i in res:
        res2.append(i)
        if (i == 10) or (i == 5):
            for x in reversed(res2):
                if x == 1:
                    res2.remove(x)
                    res2.append(-1)
        if (i == 100):
            for x in reversed(res2):
                if x == 10:
                    res2.remove(x)
                    res2.append(-10)

    return sum(res2)
