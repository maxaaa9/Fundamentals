# Write a program that reads a string from the console
#   and replaces any sequence of the same letters with a single corresponding letter.

string = input()
new_word = ""
character_check = ""
for check_letter in string:
    if check_letter != character_check:
        character_check = check_letter
        new_word += check_letter

print(new_word)
