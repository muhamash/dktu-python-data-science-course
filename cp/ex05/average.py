"""Exercise 5.2. Average of lists."""


def calculate_average(nums: list) -> float:
    """Return the average of a list of numbers.

    :param nums: list of numbers
    :return: average of list
    """
    # TODO: Code has been removed from here.
    total = 0
    for x in range(len(nums)):
        # print(nums[x])
        total = total + nums[x]
    return total / len(nums)


print(calculate_average([4, 2, 3, 1, 2]))
