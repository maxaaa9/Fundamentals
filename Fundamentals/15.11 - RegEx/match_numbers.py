import re

text = input()

pattern = r"(^|(?<= ))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?= ))"

match = re.finditer(pattern, text)

for output in match:
    print(output.group(), end=" ")
