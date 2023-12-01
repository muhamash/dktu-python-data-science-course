def truncate_values(float_list: list, settings: dict) -> list:
    """Return a truncated list of floats given the initial list and the settings for truncating. If normalize is True, the values are first normalized to the [0,1] range and then truncated.

    :param float_list: list of floats
    :param settings: Dictionary containing the keys vmin, vmax, and normalize with their corresponding values.
    :return: Truncated/Normalized+Truncated values.
    """
    vmin = settings.get("vmin")
    vmax = settings.get("vmax")
    normalize = settings.get("normalize")

    normalize_list = []
    if normalize:
        min_val = min(float_list)
        max_val = max(float_list)
        for i in float_list:
            normalize_value = (i - min_val) / (max_val - min_val)
            normalize_list.append(normalize_value)
        return normalize_list

        result = []
        for i in normalize_list:
            if i < vmin:
                result.append(vmin)
            elif i > vmax:
                result.append(vmax)
            else:
                result.append(i)
        return result

    else:
        result = []
        for i in float_list:
            if i < vmin:
                result.append(vmin)
            elif i > vmax:
                result.append(vmax)
            else:
                result.append(i)
        return result


if __name__ == "__main__":
    # here you can try out your functions
    settings = {"vmin": 0, "vmax": 0.7, "normalize": True}
    float_list = [0, 1.0, 2.0, 3.0, 4.0, 5.0]
    result = truncate_values(float_list=float_list, settings=settings)
    print(result)
