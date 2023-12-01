"""Exercise 7.5: Box packing."""


def box_packing(object: tuple, box: tuple) -> tuple:
    """Return the amount of object sticking in each dimension, or zero if sufficient space.

    :param object: Tuple (h,w) the dimensions of the object
    :param box: Tuple (H, W) the dimensions of the box.
    :return: Tuple
    """
    # TODO: Code has been removed from here.
    value_tuple = (0, 0)
    if object[0] > box[0]:
        value_tuple = (object[0] - box[0], value_tuple[1])
    if object[1] > box[0]:
        value_tuple = (value_tuple[0], object[1] - box[1])

    return value_tuple


print(box_packing((2, 5), (4, 2.1)))
