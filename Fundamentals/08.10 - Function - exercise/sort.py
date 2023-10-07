def my_sorter(integers :list) -> list:
    integer_list = []
    for i in integers:
        integer_list.append(int(i))
    sorted_list = sorted(integer_list)
    return sorted_list


sequence_of_numbers = input().split()
print(my_sorter(sequence_of_numbers))
