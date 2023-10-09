def validator(type, input):
    if type == "int":
        return int(input) * 2
    elif type == "real":
        return f"{float(input) * 1.5:.2f}"
    elif type == "string":
        return f"${input}$"


type_of_input = input()
number = input()
print(validator(type_of_input, number))