number_of_orders = int(input())
total_cost = 0
for orders in range(1, number_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    needed_capsules = int(input())
    if not 0.01 <= capsule_price <= 100.00:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= needed_capsules <= 2000:
        continue
    total_order_sum = capsule_price * days * needed_capsules
    print(f"The price for the coffee is: ${total_order_sum:.2f}")
    total_cost += total_order_sum

print(f"Total: ${total_cost:.2f}")

