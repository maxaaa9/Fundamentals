string_one = input()
string_two = input()

new_string = string_one

for i in range(len(string_one)):
    left_part = string_two[:i + 1]
    right_part = string_one[i + 1:]
    new_word = left_part + right_part
    if new_string != new_word:
        new_string = new_word
        print(new_string)
