input_string = input()
number_list = []
non_number_list = []

for index in input_string:
    if index.isdigit():
        number_list.append(index)
    else:
        non_number_list.append(index)

take_list = []
skip_list = []

for digit in range(len(number_list)):
    if digit % 2 != 0:
        skip_list.append(int(number_list[digit]))
    else:
        take_list.append(int(number_list[digit]))


non_number_string = "".join(non_number_list)
result_string = ""
for take_elements in range(len(skip_list)):
    taken_string = ""
    skipped_string = ""
    for taken in range(take_list[take_elements]):
        if taken > len(non_number_string) - 1:
            break
        taken_string += non_number_string[taken]
    result_string += taken_string
    non_number_string = non_number_string.replace(taken_string, "", 1)
    for skip in range(skip_list[take_elements]):
        if skip > len(non_number_string) - 1:
            break
        skipped_string += non_number_string[skip]
    non_number_string = non_number_string.replace(skipped_string, "", 1)

print(result_string)
