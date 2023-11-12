# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

text = input()

for emoticon in range(len(text)):
    if text[emoticon] == ":" and emoticon + 1 < len(text):
        print(f"{text[emoticon]}{text[emoticon + 1]}")
