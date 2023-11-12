# Write a program that reads a sequence of strings, separated by a single space.
#   Each string should be repeated N times, where N is the length of the string.
#       Print the final strings concatenated into one string.

sequence_of_words = input().split()
multiplied_string = ""

for word in sequence_of_words:
    length = len(word)
    multiplied_string += word * length

print(multiplied_string)
