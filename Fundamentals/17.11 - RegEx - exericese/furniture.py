import re

patters = fr">>([A-Za-z]+)<<(\d+(\.[0-9]+)?)!(\d+)\b"
total_spend_money = 0
command = input()
bought_furniture = []
while command != "Purchase":
    search = re.findall(patters, command)
    if search:
        bought_furniture.append(search[0][0])
        total_spend_money += float(search[0][1]) * int(search[0][3])
    command = input()

print("Bought furniture:")
for members in bought_furniture:
    print(members)
print(f"Total money spend: {total_spend_money:.2f}")