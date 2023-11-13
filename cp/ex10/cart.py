from cp.ex10.shopping_cart import Item


item1 = Item("Laptop", 1, 800)
item2 = Item("Phone", 1, 400)
item3 = Item("Tablet", 2, 400)

print(item1.name)
print(item1.quantity)
print(item1.price)

print(item1 < item2)
print(item2 > item3)
print(item1 == item3)
