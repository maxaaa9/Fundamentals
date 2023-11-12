# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
#   All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.


banned_words = input().split(", ")
text = input()

for check_word in banned_words:
    while check_word in text:
        new_word = ""
        for asterisks in range(len(check_word)):
            new_word += "*"
        text = text.replace(check_word, new_word)

print(text)
