from cp.ex10.shopping_cart import Inventory, Item


inventory1 = Inventory()
item1 = Item("Laptop", 10, 800)
item2 = Item("Phone", 20, 400)
item3 = Item("Tablet", 15, 300)
inventory1.add_item(item1)
inventory1.add_item(item2)
inventory1.add_item(item3)

inventory2 = Inventory()
item4 = Item("Laptop", 2, 850)
item5 = Item("Phone", 5, 420)
inventory2.add_item(item4)
inventory2.add_item(item5)

print(inventory1.calculate_total_value())
print(inventory2.calculate_total_value())
print(inventory1 > inventory2)
print(inventory1 < inventory2)
print(inventory1 == inventory2)
