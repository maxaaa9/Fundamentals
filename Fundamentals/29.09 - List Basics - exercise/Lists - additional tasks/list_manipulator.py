
initial_list = input().split()
my_digit_list = []
command = input().split()

for digit in initial_list:
    digit = int(digit)
    my_digit_list.append(digit)

while True:
    if len(command) >= 2:
        if command[1].isdigit():
            my_index = int(command[1])
    my_even_list = []
    for first_even in my_digit_list:
        if first_even % 2 == 0:
            my_even_list.append(first_even)
    my_odd_list = []
    for first_odd in my_digit_list:
        if first_odd % 2 != 0:
            my_odd_list.append(first_odd)
    if "exchange" in command:
        if my_index > len(my_digit_list) or my_index < 0:
            print("Invalid index")

        left_part = my_digit_list[:my_index + 1]
        right_part = my_digit_list[my_index + 1:]
        new_list = right_part + left_part
        my_digit_list = new_list
    elif "max" in command and "even" in command:
        max_even_list = []
        for max_even in my_digit_list:
            if max_even % 2 == 0:
                max_even_list.append(max_even)
        if len(max_even_list) >= 1:
            max_even_digit = max(max_even_list)
            max_even_digit = my_digit_list.index(max_even_digit)
            print(max_even_digit)
        else:
            print("No matches")

    elif "min" in command and "even" in command:
        min_even_list = []
        for min_even in my_digit_list:
            if min_even % 2 == 0:
                min_even_list.append(min_even)
        if len(min_even_list) >= 1:
            min_even_digit = min(min_even_list)
            min_even_digit = my_digit_list.index(min_even_digit)
            print(min_even_digit)
        else:
            print("No matches")

    elif "max" in command and "odd" in command:
        max_odd_list = []
        for max_odd in my_digit_list:
            if max_odd % 2 != 0:
                max_odd_list.append(max_odd)
        if len(max_odd_list) >= 1:
            max_odd_digit = max(max_odd_list)
            max_odd_digit = my_digit_list.index(max_odd_digit)
            print(max_odd_digit)
        else:
            print("No matches")

    elif "min" in command and "odd" in command:
        min_odd_list = []
        for even in my_digit_list:
            if even % 2 != 0:
                min_odd_list.append(even)
        if len(min_odd_list) >= 1:
            min_even_digit = min(min_odd_list)
            min_even_digit = my_digit_list.index(min_even_digit)
            print(min_even_digit)
        else:
            print("No matches")

    elif "first" in command and "even" in command:
        my_first_even_print_list = []
        if my_index > len(my_digit_list):
            print("Invalid count")
        else:
            for index_even in range(my_index):
                my_first_even_print_list.append(my_even_list[index_even])
            print(my_first_even_print_list)

    elif "first" in command and "odd" in command:
        my_first_odd_print_list = []
        if my_index > len(my_digit_list):
            print("Invalid count")
        else:
            if my_index > len(my_odd_list):
                my_index = len(my_odd_list)
            for index_odd in range(my_index):
                my_first_odd_print_list.append(my_odd_list[index_odd])
            print(my_first_odd_print_list)

    elif "last" in command and "even" in command:
        my_last_even_print_list = []
        if my_index > len(my_digit_list):
            print("Invalid count")
        else:
            for index_last_even in range(my_index):
                if len(my_even_list) >= 1:
                    my_last_even_print_list.append(my_even_list[index_last_even])
            print(my_last_even_print_list)

    elif "last" and "odd" in command:
        my_last_odd_print_list = []
        if my_index > len(my_digit_list):
            print("Invalid count")
        else:
            if my_index > len(my_odd_list):
                my_index = len(my_odd_list)
            for index_last_odd in range(my_index):
                if len(my_odd_list) >= 1:
                    my_last_odd_print_list.append(my_odd_list[index_last_odd])
            print(my_last_odd_print_list)

    command = input().split()
    if "end" in command:
        print(my_digit_list)
        break
