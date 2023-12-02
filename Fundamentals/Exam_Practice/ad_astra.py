import re

text = input()
pattern = r"([#|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"
match = re.findall(pattern, text)

total_calories = sum(int(x[3]) for x in match)
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for food_info in match:
    item_name = food_info[1]
    expiration_date = food_info[2]
    calories = food_info[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
