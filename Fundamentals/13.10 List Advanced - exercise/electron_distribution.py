number_of_electrons = int(input())

shell = 1
my_list = []
while number_of_electrons > 0:
    if 2 * shell ** 2 < number_of_electrons:
        my_list.append(2 * shell ** 2)
        number_of_electrons -= 2 * shell ** 2
    else:
        my_list.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
    shell += 1

print(my_list)