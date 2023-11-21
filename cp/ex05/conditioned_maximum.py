"""Exercise 5.3-5.4. Conditioned maximum."""


def conditioned_maximum(nums: list, threshold: float) -> float:
    """Return the maximum of a list of numbers, that is strictly smaller than the given threshold.

    :param nums: list of numbers
    :param threshold: limit for maximum value
    :return: maximum of list thats smaller than the threshold
    """
    # TODO: Code has been removed from here.
    count = 0
    for x in nums:
        # print(nums[x])
        if threshold > x:
            count = count + 1
    return count


# result = conditioned_maximum([1, 2, 3, 4, 5], 10)
# print(result)


def conditioned_maximum_name(nums: list, names: list, threshold: float) -> str:
    """Return the name of the maximum of a list of numbers, that is smaller than the given threshold.

    :param nums: list of numbers with animal heights.
    :param names: list of animal names
    :param threshold: limit for maximum value
    :return: animal name with the corresponding maximum height, which is shorter than the threshold height.
    """
    # TODO: Code has been removed from here.
    max_height = 0
    animal_name = ""

    for i in range(len(nums)):
        if nums[i] < threshold and nums[i] > max_height:
            max_height = nums[i]
            animal_name = names[i]
    return animal_name


heights = [1.5, 1.6, 5.5, 3.0, 2.5, 1.0, 1.4]
names = ["cow", "horse", "giraffe", "elephant", "dinosaur", "dog", "dear"]
print(conditioned_maximum_name(heights, names, 3.0))
