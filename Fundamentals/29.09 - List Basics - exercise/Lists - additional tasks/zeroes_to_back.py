my_input = input().split(", ")

for checker in range(len(my_input)):
    for check in range(len(my_input)):
        if my_input[check] == "0":
            my_input.append(my_input.pop(check))
integer_list = []
for integers in range(len(my_input)):
    integer_list.append(int(my_input[integers]))

print(integer_list)