"""Exercise 5.8.-5-9. Count multiples."""


def count_multiples(numbers: list, m: int) -> int:
    """Count the number of numbers that are divisible by m.

    :param numbers: list of numbers
    :param m: number to divide by
    :return: number of numbers that are divisible by m
    """
    # TODO: Code has been removed from here.
    count = 0
    for num in numbers:
        if num % m == 0:
            count = count + 1
    return count


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count_multiples(a, 2))


def multiples_list(numbers: list, m: int) -> list:
    """Make a list with all numbers from a list that are divisible by m.

    :param numbers: list of numbers
    :param m: number to divide by
    :return: list of numbers that are divisible by m
    """
    # TODO: Code has been removed from here.
    # multiples = []
    # for i in numbers:
    #     if i % m == 0:
    #         multiples.append(i)
    # return multiples

    multiples = [i for i in numbers if i % m == 0]
    return multiples


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(multiples_list(a, 3))
