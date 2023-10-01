train_ticket_price = 150

my_collection = input().split("|")
start_budget = float(input())
profit = 0
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
budget = start_budget
for items in range(len(my_collection)):
    splitter = my_collection[items].split("->")
    item = splitter[0]
    cost = float(splitter[1])
    cost_validator = False
    if cost <= budget:
        if item == "Clothes" and 0 <= cost <= clothes_max_price:
            budget -= cost
            profit += cost
            cost_validator = True
        elif item == "Shoes" and 0 <= cost <= shoes_max_price:
            budget -= cost
            profit += cost
            cost_validator = True
        elif item == "Accessories" and 0 <= cost <= accessories_max_price:
            budget -= cost
            profit += cost
            cost_validator = True
        if cost_validator:
            print(f"{(cost * 1.4):.2f}", end=" ")
print()
profit = profit * 1.4 - profit
print(f"Profit: {profit:.2f}")
if profit + start_budget >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")