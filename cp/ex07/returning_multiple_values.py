"""Exercise 7.4: Returning multiple values."""


def returning_multiple_values(values: list, threshold: int) -> tuple:
    """Return a tuple containing a list of all elements in the list that are greater than the threshold and the minimum of the values.

    :param values: A list of integers.
    :param threshold: An integer.
    :return: A tuple containing the a list of elements that are greater than the threshold and the minimum of values
    """
    # TODO: Code has been removed from here.
    new_list = []

    for i in values:
        if i > threshold:
            new_list.append(i)
    # return new_list
    min_val = min(values)
    # print(min_val)

    return new_list, min_val


# print(returning_multiple_values([3, 2.4, 1.2, 4.3, -0.5], 2))
threshold_list, minimum_value = returning_multiple_values([3, 2.4, 1.2, 4.3, -0.5], 2)
print(minimum_value)
print(threshold_list)
