
sequence_of_integers = list(map(int, input().split()))
removed_elements = []
while len(sequence_of_integers) > 0:
    command_index = int(input())

    if command_index < 0:
        popped_element = sequence_of_integers.pop(0)
        sequence_of_integers.insert(0, sequence_of_integers[-1])

    elif command_index > len(sequence_of_integers) - 1:
        popped_element = sequence_of_integers.pop(-1)
        sequence_of_integers.append(sequence_of_integers[0])

    else:
        popped_element = sequence_of_integers.pop(command_index)
    removed_elements.append(popped_element)
    for num in range(len(sequence_of_integers)):
        if popped_element >= sequence_of_integers[num]:
            sequence_of_integers[num] += popped_element
        else:
            sequence_of_integers[num] -= popped_element

print(sum(removed_elements))
