"""Exercise 7.3: Last difference."""


def last_difference(a: tuple, b: tuple) -> float:
    """Return the difference between last elements regardless of length.

    :param a: The first tuple.
    :param b: The second tuple.
    :return: The difference between the last elements of the two tuples.
    """
    # TODO: Code has been removed from here.
    last_a = a[-1]
    last_b = b[-1]

    difference = last_a - last_b
    return difference


result = last_difference((12, 25, 17.6), (14, 12.1, 18, -6.7))
print(result)
