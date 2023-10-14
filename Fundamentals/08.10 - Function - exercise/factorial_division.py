def factorial(number: int) -> float:
    for i in range(1, number):
        number *= i

    return number


first_number = int(input())
divider = int(input())
result = factorial(first_number) / factorial(divider)
print(f"{result:.2f}")