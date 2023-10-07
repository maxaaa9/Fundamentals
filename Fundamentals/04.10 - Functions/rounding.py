def rounding(numbers) -> list:
    numbers = numbers.split()
    my_list = []
    for i in numbers:
        i = float(i)
        my_list.append(round(i))
    print(my_list)
    return my_list


given_numbers = input()
rounding(given_numbers)


