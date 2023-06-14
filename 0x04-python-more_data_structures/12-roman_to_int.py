#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    if not isinstance(roman_string, str):
        return 0
    for index, x in enumerate(roman_string):
        if index == 0:
            index = 1
        past_x = roman_string[index - 1]
        if roman[x] > roman[past_x]:
            number = number + (roman[x] - roman[past_x] * 2)
        else:
            number = number + roman[x]
    return number
