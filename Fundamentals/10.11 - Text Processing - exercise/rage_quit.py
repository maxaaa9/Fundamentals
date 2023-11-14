input_string = input()

new_word = ""
word = ""
for check_word in range(len(input_string)):
    digit = ""
    if input_string[check_word].isdigit():
        for digits in range(check_word, len(input_string)):
            if input_string[digits].isdigit():
                digit += input_string[digits]
            else:
                break
        new_word += int(digit) * word
        word = ""

    else:
        word += input_string[check_word].upper()


print(f"Unique symbols used: {len(set(new_word))}")
print(new_word)

