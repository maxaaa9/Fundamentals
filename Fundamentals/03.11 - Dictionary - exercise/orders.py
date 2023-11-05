# Write a program that keeps the information about products and their prices.
#   Each product has a name, a price, and a quantity:
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists,
#   increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines.
#   Until you receive the command "buy", keep adding items. Finally,
#       print all items with their names and the total price of each product.

my_products = {}
while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in my_products.keys():
        my_products[name] = [price, quantity]
    else:
        my_products[name][0] = price
        my_products[name][1] += quantity

for product, total_price in my_products.items():
    total_price = total_price[0] * total_price[1]
    print(f"{product} -> {total_price:.2f}")
