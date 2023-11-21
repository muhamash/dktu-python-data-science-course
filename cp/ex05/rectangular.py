"""Exercise 5.6. Rectangular list."""


def is_rectangular(nested_list: list) -> bool:
    """Check if a list is rectangular.

    :param nested_list: nested list
    :return: True if list is rectangular, False otherwise
    """
    # TODO: Code has been removed from here.
    if not nested_list:
        return False

    first_sub_list = len(nested_list[0])
    print(f"len of first_sub_list:{first_sub_list}")

    for sublist in nested_list:
        if len(sublist) != first_sub_list:
            return False
    return True


print(is_rectangular([[1, 2, 3, 4], ["cat", "dog", "mouse"]]))
