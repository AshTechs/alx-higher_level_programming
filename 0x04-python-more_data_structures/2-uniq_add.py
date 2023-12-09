#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    total = 0
    for num in my_list:
        if num not in seen:
            seen.add(num)
            total += num
    return total
