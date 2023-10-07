my_input_as_string = input().split()
my_input_as_digits = []

for number in my_input_as_string:
    my_input_as_digits.append(int(number))

output = list(filter(lambda x: x % 2 == 0, my_input_as_digits))
print(output)

# def even_checker(string_numbers: str) -> list:
#     my_list = string_numbers.split()
#     even_list = []
#     for even in my_list:
#         even = int(even)
#         if even % 2 == 0:
#             even_list.append(even)
#
#     return even_list
#
# my_input = input()
# print(even_checker(my_input))