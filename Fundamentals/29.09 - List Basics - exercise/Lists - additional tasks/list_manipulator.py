def exchanger(int_list, idx) -> list:
    if idx > len(int_list) - 1 or idx < 0:
        print("Invalid index")
        return int_list
    int_list = int_list[idx + 1:] + int_list[:idx + 1]
    return int_list


def odd_or_even(list_of_ints, even_or_odd):
    if status == "even":
        even_list = [x for x in list_of_ints if x % 2 == 0]
        return even_list
    elif status == "odd":
        odd_list = [x for x in list_of_ints if x % 2 != 0]
        return odd_list


def first_last(integer_list, counter, status, action):
    if status == "even":
        integer_list = odd_or_even(integer_list, status)
    elif status == "odd":
        integer_list = odd_or_even(integer_list, status)
    print_list = []
    if action == "first":
        for first_digits in integer_list:
            if len(print_list) < counter:
                print_list.append(first_digits)
            else:
                break

    elif action == "last":
        integer_list = integer_list[::-1]
        for last_digits in integer_list:
            if len(print_list) < counter:
                print_list.append(last_digits)
            else:
                break
        print_list = print_list[::-1]
    print(print_list)


def rightmost_element(list_with_nums, main_int_list, number, operation):
    max_index = 0
    for right_index, num in enumerate(main_int_list):
        if operation == "max":
            if num >= number and num in list_with_nums:
                max_num = num
                max_index = right_index
        else:
            if num <= number and num in list_with_nums:
                max_num = num
                max_index = right_index
    return max_index


line_of_integers = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "exchange":
        index = int(command[1])
        line_of_integers = exchanger(line_of_integers, index)

    elif command[0] == "max" or command[0] == "min":
        status = command[1]  #even or odd
        status_list = odd_or_even(line_of_integers, status)
        if len(status_list) <= 0:
            print("No matches")
            continue
        if command[0] == "max":
            max_num = max(status_list)
            result_index = rightmost_element(status_list, line_of_integers, max_num, command[0])
            print(result_index)
        elif command[0] == "min":
            min_num = min(status_list)
            result_index = rightmost_element(status_list, line_of_integers, min_num, command[0])
            print(result_index)

    elif command[0] == "first" or command[0] == "last":
        count = int(command[1])
        status = command[2]
        action = command[0]
        if count > len(line_of_integers):
            print("Invalid count")
            continue
        first_last(line_of_integers, count, status, action)


print(line_of_integers)
