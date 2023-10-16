my_list = int(input())

if my_list == 0:
    my_list_with_integers = []
elif my_list == 1:
    my_list_with_integers = [1]
elif my_list == 2:
    my_list_with_integers = [1, 1]
else:
    my_list_with_integers = [1, 1, 2]
    for i in range(3, my_list):
        next_number = my_list_with_integers[i - 1] + my_list_with_integers[i - 2] + my_list_with_integers[i - 3]
        my_list_with_integers.append(next_number)

my_list_with_integers = list(map(str, my_list_with_integers))
print(" ".join(my_list_with_integers))
