# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.

import re

text = input()
find_word = input()
pattern = fr"(?i)\b({find_word})+\b"
match = re.findall(pattern, text)
print(len(match))

