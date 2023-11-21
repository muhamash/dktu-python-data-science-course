"""Exercise 5.7. Vector additon."""


def vector_add(v: list, w: list) -> list:
    """Add two vectors.

    :param v: vector 1 (list of numbers)
    :param w: vector 2 (list of numbers, same length as v)
    :return: sum of v and w (list of number)
    """
    # TODO: Code has been removed from here.
    if len(v) != len(w):
        print("error")
        return []

    result = []
    for i in range(len(v)):
        result.append(v[i] + w[i])
        # print(v[i], w[i])
    return result


a = [1, 2, 3]
b = [4, 5, 6]
print(vector_add(a, b))
