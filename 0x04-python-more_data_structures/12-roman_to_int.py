#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
                          'X': 10, 'V': 5, 'I': 1}
        numbers = []
        index = 0
        total = 0
        for index in roman_string:
            for numeral, integer in roman_numerals.items():
                if index is numeral:
                    numbers.append(integer)
        for i, num in enumerate(numbers):
            total += num
            if i < len(numbers) - 1:
                if num < numbers[i + 1]:
                    total -= (num * 2)
        return total
    return 0
