number_of_cities = int(input())
total_profit = 0
for city in range(1, number_of_cities + 1):
    name = input()
    money = float(input())
    expenses = float(input())
    if city % 5 == 0:
        money *= 0.9

    elif city % 3 == 0:
        expenses *= 1.5

    profit = money - expenses
    total_profit += profit
    print(f"In {name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")