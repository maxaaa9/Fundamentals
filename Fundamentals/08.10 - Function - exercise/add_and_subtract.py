def sum_numbers(one, two) -> int:
    return one + two


def subtract(sum_of_two_integers, subtract_integer) -> int:
    return sum_of_two_integers - subtract_integer


def add_and_subtract(first_int, second_int, third_int) -> int:
    difference = subtract(sum_numbers(first_int, second_int), third_int)
    return difference


integer_one = int(input())
integer_two = int(input())
integer_three = int(input())
print(add_and_subtract(integer_one, integer_two, integer_three))
