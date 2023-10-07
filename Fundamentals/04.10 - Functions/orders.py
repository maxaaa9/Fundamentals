def order_calculator(drink_type, number) -> float:
    price_of_drink = 0
    if drink_type == "coffee":
        price_of_drink = 1.50
    elif drink_type == "coke":
        price_of_drink = 1.40
    elif drink_type == "water":
        price_of_drink = 1.00
    elif drink_type == "snacks":
        price_of_drink = 2.00

    total_sum = float(price_of_drink * number)
    print(f"{total_sum:.2f}")
    return total_sum


consumption = input()
quantity = int(input())
order_calculator(consumption, quantity)
