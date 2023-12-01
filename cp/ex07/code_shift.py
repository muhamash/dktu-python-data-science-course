"""Exercise 7.7: Code shift."""


def code_shift(code: tuple, turn: tuple) -> tuple:
    """Return the updated code pattern.

    :param code: Tuple with the initial code in the lock
    :param turn: Tuple with the turn on each lock dial
    :return: Updated lock code.
    """
    # TODO: Code has been removed from here.
    dial_lock = list(code)

    for i in range(4):
        dial_lock[i] = (dial_lock[i] + turn[i]) % 10
    return tuple(dial_lock)


print(code_shift((9, 9, 9, 9), (1, -1, 2, -2)))
