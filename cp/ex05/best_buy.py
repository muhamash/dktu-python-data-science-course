"""Exercise 5.11. Best Buy."""


def best_buy(prices: list, money: int, start_index: int, reverse: bool) -> int:
    """Return the number of items that can be bought with the given amount of money. The function should be able to handle arbitrary starting points and to run the list in reverse.

    :param prices: list of prices
    :param money: amount of money
    :param start_index: starting index in list
    :param reverse: boolean to indicate if list should be run in reverse
    :return: number of items that can be bought with the given amount of money
    """
    # TODO: Code has been removed from here.
    items_bought = 0
    index = start_index
    length = len(prices)

    if reverse:
        direction = -1
        end_direction = -1
    else:
        direction = 1
        end_direction = length

    for _ in range(abs(end_direction - start_index)):
        if money >= prices[index]:
            money -= prices[index]
            items_bought = items_bought + 1
        else:
            break

        index = (index + direction) % length
    return items_bought


prices = [3, 2, 1, 3, 5]
print(best_buy(prices, 10, 4, True))
