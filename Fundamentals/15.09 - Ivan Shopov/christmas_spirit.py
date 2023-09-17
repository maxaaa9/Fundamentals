quantity_of_decoration = int(input())
days_left_until_christmas = int(input())

ornament_set = 2
skirt = 5
garland = 3
light = 15

total_cost = 0
total_spirit = 0

for days in range(1, days_left_until_christmas + 1):
    if days % 11 == 0:
        quantity_of_decoration += 2
    if days % 2 == 0:
        total_cost += ornament_set * quantity_of_decoration
        total_spirit += 5
    if days % 3 == 0:
        total_cost += (skirt + garland) * quantity_of_decoration
        total_spirit += 13
    if days % 5 == 0:
        total_cost += light * quantity_of_decoration
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_cost += (skirt + garland + light)


if days_left_until_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")


