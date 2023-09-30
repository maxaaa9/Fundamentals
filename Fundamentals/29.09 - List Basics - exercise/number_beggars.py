string_of_integers = input().split(", ")
number_of_beggars = int(input())
my_list_with_integers = []

for integers in string_of_integers:
    my_list_with_integers.append(int(integers))

start_index = 0
sum_for_beggars = []
while start_index < number_of_beggars:
    current_beggar_sum = 0
    for beggar in range(start_index, len(my_list_with_integers), number_of_beggars):
        current_beggar_sum += my_list_with_integers[beggar]
    sum_for_beggars.append(current_beggar_sum)
    start_index += 1

print(sum_for_beggars)