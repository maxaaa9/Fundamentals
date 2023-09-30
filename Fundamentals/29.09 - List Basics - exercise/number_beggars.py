string_with_integers = input().split(", ")
number_of_beggars = int(input())
my_integer_list = []
for integers in range(len(string_with_integers)):
    my_integer_list.append(int(string_with_integers[integers]))

total_coins_per_beggar = []
my_index_for_beggars = 0
while my_index_for_beggars < number_of_beggars:
    current_beggar_coin = 0
    for coin in range(my_index_for_beggars, len(my_integer_list), number_of_beggars):
        current_beggar_coin += my_integer_list[coin]
    total_coins_per_beggar.append(current_beggar_coin)
    my_index_for_beggars += 1
print(total_coins_per_beggar)
