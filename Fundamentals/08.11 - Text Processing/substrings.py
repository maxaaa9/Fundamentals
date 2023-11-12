# On the first line, you will receive a string.
#   On the second line, you will receive a second string.
#       Write a program that removes all the occurrences of the first string in the second until there is no match.
#           At the end, print the remaining string.

remove_word = input()
word = input()

while remove_word in word:
    word = word.replace(remove_word, "")

print(word)
