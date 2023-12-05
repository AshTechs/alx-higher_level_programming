#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    
    sum_1 = tuple_a[0] if len_a >= 1 else 0
    sum_2 = tuple_a[1] if len_a >= 2 else 0
    sum_3 = tuple_b[0] if len_b >= 1 else 0
    sum_4 = tuple_b[1] if len_b >= 2 else 0
    
    new_tuple = (sum_1 + sum_3 sum_2 + sum_4)
    
    return new_tuple
