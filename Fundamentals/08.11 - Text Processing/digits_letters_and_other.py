# Write a program that receives a single string.
#   On the first line, print all the digits found in the string, on the second – all the letters,
#       and on the third – all the other characters. There will always be at least one digit, one letter,
#           and one other character.

word = input()
digits = "".join([x for x in word if x.isdigit()])
letters = "".join([x for x in word if x.isalpha()])
other = "".join([x for x in word if not x.isdigit() and not x.isalpha()])

# for check in word:
#     if check.isdigit():
#         digits += check
#     elif check.isalpha():
#         letters += check
#     else:
#         other += check

print(f"{digits}\n{letters}\n{other}")
