#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    X = 10 / VII = 7  / IX = 9 /
    LXXXVII = 87 / DCCVII = 707
    """
    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    res = [roman_numeral.get(i) for i in roman_string]
    i = 0
    res2 = []
    for i in res:
        res2.append(i)
        if i == 10:
            for x in reversed(res2):
                if x == 1:
                    res2.remove(x)
                    res2.append(-1)

    return (sum(res2))
