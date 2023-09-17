budget = float(input())

price_for_flour = float(input())
price_for_eggs = price_for_flour * 0.75
price_for_milk = price_for_flour * 1.25

total_price_for_bread = price_for_flour + price_for_eggs + price_for_milk / 4

loaves_of_bread = 0
eggs_counter = 0


while budget > total_price_for_bread:
    budget -= total_price_for_bread
    loaves_of_bread += 1
    eggs_counter += 3
    if loaves_of_bread % 3 == 0:
        eggs_counter -= loaves_of_bread - 2

print(f"You made {loaves_of_bread} loaves of Easter bread! Now you have {eggs_counter:} eggs and {budget:.2f}BGN left.")
