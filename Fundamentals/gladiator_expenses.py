lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses_for_repair = 0

for lost in range(1, lost_fight + 1):
    if lost % 2 == 0:
        expenses_for_repair += helmet_price
    if lost % 3 == 0:
        expenses_for_repair += sword_price
    if lost % (2 * 3) == 0:
        expenses_for_repair += shield_price
    if lost % (2 * 3 * 2) == 0:
        expenses_for_repair += armor_price

print(f"Gladiator expenses: {expenses_for_repair:.2f} aureus")
