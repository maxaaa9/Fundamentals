# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

my_word = [x for x in input() if x != " "]
char_dictionary = {}

for word in my_word:
    if word not in char_dictionary:
        char_dictionary[word] = 0
    char_dictionary[word] += 1

for char, nums in char_dictionary.items():
    print(f"{char} -> {nums}")
