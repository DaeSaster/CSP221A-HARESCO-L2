orders = [
    ("Laptop", 2, 350),
    ("Mouse", 5, 20),
    ("Monitor", 3, 220)
]

def add_order(order_data, product_name, quantity, price):
    new_order = (product_name, quantity, price)
    order_data.append(new_order)

add_order(orders, "Keyboard", 5, 1000)
add_order(orders, "Fan", 2, 30)

print(orders)

high_value_items = []

for product_name, quantity, price in orders:
    total_price = quantity * price

    if total_price > 500:
        high_value_items.append(product_name)
        print(high_value_items, total_price)