#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    result = []
    for num in my_list:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
