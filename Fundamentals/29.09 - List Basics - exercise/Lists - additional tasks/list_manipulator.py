def exchange(my_list, index) -> list:
    for split in range(index + 1):
        split = 0
        popper = my_list.pop(split)
        my_list.append(popper)
    return my_list


def index_validator(my_list, check_index):
    check_index = int(check_index)
    if check_index >= len(my_list) or check_index < 0:
        return True
    return False


def max_even_or_odd(my_list, odd_or_even) -> str:
    if odd_or_even == "odd":
        max_odd_list = [x for x in my_list if x % 2 != 0]
        if len(max_odd_list) >= 1:
            return str(max(max_odd_list))
    elif odd_or_even == "even":
        max_even_list = [x for x in my_list if x % 2 == 0]
        if len(max_even_list) >= 1:
            return str(max(max_even_list))
    return odd_or_even


def min_even_or_odd(my_list, odd_or_even) -> str:
    if odd_or_even == "odd":
        min_odd_list = [x for x in my_list if x % 2 != 0]
        if len(min_odd_list) >= 1:
            return str(min(min_odd_list))

    elif odd_or_even == "even":
        min_even_list = [x for x in my_list if x % 2 == 0]
        if len(min_even_list) >= 1:
            return str(min(min_even_list))
    return odd_or_even


def rightmost_element(check_list, digit) -> int:
    index_of_rightmost = 0
    for index, num in enumerate(check_list):
        if num == int(digit):
            index_of_rightmost = index
    return index_of_rightmost


def first_odd_or_even(my_list, first_count, even_or_odd) -> list:
    first_odd_or_even_list = []
    needed_numbers = 1
    if even_or_odd == "even":
        for check_even in my_list:
            if check_even % 2 == 0 and needed_numbers <= first_count:
                first_odd_or_even_list.append(check_even)
                needed_numbers += 1
    elif even_or_odd == "odd":
        for check_odd in my_list:
            if check_odd % 2 != 0 and needed_numbers <= first_count:
                first_odd_or_even_list.append(check_odd)
                needed_numbers += 1
    return first_odd_or_even_list


def last_odd_or_even(my_list, last_count, even_or_odd) -> list:
    last_odd_or_even_list = []
    needed_numbers = 1
    if even_or_odd == "even":
        for check_even in range(len(my_list)-1, -1, -1):
            if my_list[check_even] % 2 == 0 and needed_numbers <= last_count:
                last_odd_or_even_list.append(my_list[check_even])
                needed_numbers += 1
    elif even_or_odd == "odd":
        for check_odd in range(len(my_list)-1, -1, -1):
            if my_list[check_odd] % 2 != 0 and needed_numbers <= last_count:
                last_odd_or_even_list.append(my_list[check_odd])
                needed_numbers += 1
    return last_odd_or_even_list


sequence_of_numbers = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        print(sequence_of_numbers)
        break

    elif command[0] == "exchange":
        if len(command) > 1:
            if index_validator(sequence_of_numbers, command[1]):
                print("Invalid index")
                continue
        exchange_numbers = int(command[1])
        sequence_of_numbers = exchange(sequence_of_numbers, exchange_numbers)
        continue
    elif command[0] == "max":
        check_max_digit_index = max_even_or_odd(sequence_of_numbers, command[1])
        if check_max_digit_index.isdigit():
            rightmost_index = rightmost_element(sequence_of_numbers, check_max_digit_index)
            print(rightmost_index)
        else:
            print("No matches")
        continue
    elif command[0] == "min":
        check_min_digit_index = min_even_or_odd(sequence_of_numbers, command[1])
        if check_min_digit_index.isdigit():
            rightmost_index = rightmost_element(sequence_of_numbers, check_min_digit_index)
            print(rightmost_index)
        else:
            print("No matches")
        continue
    elif command[0] == "first":
        count_numbers = int(command[1])
        if count_numbers > len(sequence_of_numbers):
            print("Invalid count")
            continue
        else:
            print(first_odd_or_even(sequence_of_numbers, count_numbers, command[2]))
    elif command[0] == "last":
        count_numbers = int(command[1])
        if count_numbers > len(sequence_of_numbers):
            print("Invalid count")
            continue
        else:
            print(last_odd_or_even(sequence_of_numbers, count_numbers, command[2]))



