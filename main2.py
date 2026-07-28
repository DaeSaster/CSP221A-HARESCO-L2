def add_order(orders, item, quantity, price):
    orders.append((item, quantity, price))


orders = []

add_order(orders, "Laptops", 2, 350)
add_order(orders, "Mouse", 5, 20)
add_order(orders, "Monitor", 3, 220)
add_order(orders, "Keyboard", 5, 1000)
add_order(orders, "Fan", 2, 30)

print(orders)

high_value_items = []

for item, quantity, price in orders:
    total = quantity * price

    if total > 500:
        high_value_items.append(item)
        print(high_value_items, total)
