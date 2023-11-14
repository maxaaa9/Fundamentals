number_of_lines = int(input())

for strings in range(number_of_lines):
    text = input()
    name = ""
    age = ""
    for area in text:
        if area == "@":
            name = text[text.index(area) + 1:]
        elif area == "|":
            name = name[:name.index(area)]
        elif area == "#":
            age = text[text.index(area) + 1:]
        elif area == "*":
            age = age[:age.index(area)]
    print(f"{name} is {age} years old.")