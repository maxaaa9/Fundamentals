import re

count_of_strings = int(input())
pattern = r"\!([A-Z][a-z]{2,})\!:\[([A-Za-z]{8,})\]"
for strings in range(count_of_strings):
    text = input()
    match = re.fullmatch(pattern, text)
    if not match:
        print("The message is invalid")
        continue
    ord_list = []
    for decode in match.group(2):
        ord_list.append(str(ord(decode)))
    print(f"{match.group(1)}: {' '.join(ord_list)}")