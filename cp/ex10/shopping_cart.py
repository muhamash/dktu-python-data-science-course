"""This file contains the project's code and solution."""


class Item:
    """A class to represent an inventory item."""

    # TODO: Code has been removed from here.
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __lt__(self, other):
        return (self.quantity * self.price) < (other.quantity * other.price)

    def __gt__(self, other):
        return (self.quantity * self.price) > (other.quantity * other.price)

    def __eq__(self, other):
        return (self.quantity * self.price) == (other.quantity * other.price)


class Inventory:
    """A class to represent an inventory of items."""

    # TODO: Code has been removed from here.
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_value(self):
        return sum(item.quantity * item.price for item in self.items)

    def __lt__(self, other):
        return self.calculate_total_value() < other.calculate_total_value()

    def __gt__(self, other):
        return self.calculate_total_value() > other.calculate_total_value()

    def __eq__(self, other):
        return self.calculate_total_value() == other.calculate_total_value()
