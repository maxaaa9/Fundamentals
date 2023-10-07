def min_max_sum(numbers: list) -> str:
    my_integer_list = []
    for integer in numbers:
        my_integer_list.append(int(integer))
    sum_list = [min(my_integer_list), max(my_integer_list)]
    my_output = f"The minimum number is {min(sum_list)}\n" \
                f"The maximum number is {max(sum_list)}\n" \
                f"The sum number is: {sum(my_integer_list)}"
    print(my_output)
    return my_output


sequence_of_numbers = input().split()
min_max_sum(sequence_of_numbers)
