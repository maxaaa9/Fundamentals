list_sequence = input().split()
my_even_strings = [x for x in list_sequence if len(x) % 2 == 0]
my_even_strings = "\n".join(my_even_strings)
print(my_even_strings)
