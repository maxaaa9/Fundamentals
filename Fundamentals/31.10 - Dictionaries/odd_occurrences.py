# Write a program that prints all elements from a given sequence of words that
#   occur an odd number of times (case-insensitive) in it.
# ⦁	Words are given on a single line, space-separated.
# ⦁	Print the result elements in lowercase, in their order of appearance.

sequence_of_words = input().split()
odd_dictionary = {}

for check in sequence_of_words:
    check = check.lower()
    if check not in odd_dictionary:
        odd_dictionary[check] = 1
    else:
        odd_dictionary[check] += 1

for key, value in odd_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
