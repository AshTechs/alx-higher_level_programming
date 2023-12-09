#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    nums = []

    for char in roman_string:
        if char in roman_values:
            nums.append(roman_values[char])

 sum(nums)
