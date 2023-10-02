sequence_number = input().split()
my_text = input()
my_list = list(my_text)
word = ""
for i in sequence_number:
    total_sum = 0
    for sum_of_digit in i:
        total_sum += int(sum_of_digit)
    check_index = total_sum % len(my_text)
    my_word = my_text[check_index]
    word += my_word
    my_list.pop(check_index)
    my_text = my_list

print(word)