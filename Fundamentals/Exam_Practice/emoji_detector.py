import re

text = input()
pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
digit_pattern = r"\d"
matched_emoji = [x for x in re.findall(pattern, text,)]
all_digits = list(map(int, re.findall(digit_pattern, text)))
coolness = 1
for sum_coolness in all_digits:
    coolness *= sum_coolness
emoji_dictionary = {}
for emoji in matched_emoji:
    emoji_coolness = 0
    for ascii_sum in emoji:
        if ascii_sum.isalpha():
            emoji_coolness += ord(ascii_sum)
    if emoji_coolness > coolness:
        emoji_dictionary[emoji] = emoji_coolness

print(f"Cool threshold: {coolness}")
print(f"{(len(matched_emoji))} emojis found in the text. The cool ones are:")
if emoji_dictionary:
    for cool_emoji, score in emoji_dictionary.items():
        print(cool_emoji)
