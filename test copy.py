items = [{"name": "Laptop", "price": 899.99}, {"name": "Keyboard", "price": 75.00}]
prices = []
for item in items:
    price = item.get("price")
    prices.append(price)
print(prices)


