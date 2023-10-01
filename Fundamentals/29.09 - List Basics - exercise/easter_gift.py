names_of_gifts = input().split()
command = input()

while command != "No Money":
    gifts = command.split()
    status = gifts[0]
    product = gifts[1]
    if product in names_of_gifts or status != "OutOfStock":
        if len(gifts) >= 3:
            quantity = gifts[2]
            quantity = int(quantity)
            if status == "Required":
                if len(names_of_gifts) > quantity >= 0:
                    names_of_gifts[quantity] = product
        if status == "OutOfStock":
            for check in range(len(names_of_gifts)):
                if names_of_gifts[check] == product:
                    names_of_gifts[check] = "None"
        elif status == "JustInCase":
            names_of_gifts.pop()
            names_of_gifts.append(product)
    command = input()
while 'None' in names_of_gifts:
    names_of_gifts.remove("None")

my_string_output = " ".join(names_of_gifts)

print(my_string_output)