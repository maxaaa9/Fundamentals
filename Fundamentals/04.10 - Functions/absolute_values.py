def absolute_value(sequence: str) -> [list]:
    sequence = sequence.split()
    my_list = []
    for integer in sequence:
        my_list.append(abs(float(integer)))

    return print(my_list)


sequence_of_numbers = input()
absolute_value(sequence_of_numbers)
