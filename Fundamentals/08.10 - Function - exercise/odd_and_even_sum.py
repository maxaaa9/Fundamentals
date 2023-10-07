def sum_of_all_even_and_odd_digits(number: int) -> str:
    number = str(number)
    number.split()
    odd_number = 0
    even_number = 0
    for check in number:
        check = int(check)
        if check % 2 == 0:
            even_number += check
        else:
            odd_number += check
    output = f"Odd sum = {odd_number}, Even sum = {even_number}"
    return output


single_number = int(input())
print(sum_of_all_even_and_odd_digits(single_number))
