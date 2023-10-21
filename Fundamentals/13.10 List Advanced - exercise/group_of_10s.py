my_sequence_list = [int(x) for x in input().split(", ")]
group = 10

while my_sequence_list:
    my_list = [number for number in my_sequence_list if number <= group]
    print(f"Group of {group}'s: {my_list}")
    my_sequence_list = [number for number in my_sequence_list if number > group]
    group += 10
