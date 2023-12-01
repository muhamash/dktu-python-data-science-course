"""Exercise 7.4: Color Hue."""


def rgb_to_hue(RGB: tuple) -> float:
    """Return the hue given RGB values.

    :param RGB: Tuple containing  three RGB values.
    :return: Hue in degrees.
    """
    # TODO: Code has been removed from here.
    R, G, B = RGB

    max_value = max(R, G, B)
    min_value = min(R, G, B)

    if max_value == min_value:
        return 0

    if max_value == R:
        H = (60 * ((G - B) / (max_value - min_value)) + 360) % 360
    elif max_value == G:
        H = 60 * ((B - R) / (max_value - min_value)) + 120
    elif max_value == B:
        H = 60 * ((B - R) / (max_value - min_value)) + 240
    return H


RGB = (0.6, 0.2, 0.3)
print(rgb_to_hue(RGB))
