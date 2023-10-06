#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least two elements
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]

    # Add corresponding elements of the tuples and return a new tuple
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
