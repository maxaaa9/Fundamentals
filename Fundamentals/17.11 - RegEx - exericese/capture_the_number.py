# Write a program that receives strings on different lines and extracts only the numbers.
#   Print all extracted numbers on a single line, separated by a single space.

import re

text = input()
my_list = []
pattern = r"\d+"
while text:
    match = re.findall(pattern, text)
    if match:
        my_list.append(match)
    text = input()

for numbers in my_list:
    print(" ".join(numbers), end=" ")
