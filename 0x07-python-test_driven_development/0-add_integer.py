def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")
    a = int(a) if not isinstance(a, int) else a
    b = int(b) if not isinstance(b, int) else b
    return a + b

