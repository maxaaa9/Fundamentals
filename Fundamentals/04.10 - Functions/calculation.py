def calculator(first_integer, action, second_integer) -> int:
    first_integer = int(first_integer)
    second_integer = int(second_integer)
    result = 0
    if action == "multiply":
        result = first_integer * second_integer
    elif action == "divide":
        result = first_integer / second_integer
    elif action == "add":
        result = first_integer + second_integer
    elif action == "subtract":
        result = first_integer - second_integer

    return int(result)


operator = input()
integer_one = input()
integer_two = input()
print(calculator(integer_one, operator, integer_two))
