foods = input().split()
my_dict = {}

for check in range(0, len(foods), 2):
    key = foods[check]
    value = int(foods[check + 1])
    my_dict[key] = value

print(my_dict)