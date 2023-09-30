my_list_as_string = input().split()
numbers_to_remove = int(input())

my_integer_list = []
for integers in range(len(my_list_as_string)):
    my_integer_list.append(int(my_list_as_string[integers]))

my_sorted_list = my_integer_list.copy()
my_sorted_list.sort()

for smallest in range(numbers_to_remove):
    if my_sorted_list[smallest] in my_integer_list:
        my_integer_list.remove(my_sorted_list[smallest])
string_list = []
for output in range(len(my_integer_list)):
    string_list.append(str(my_integer_list[output]))
my_output = ", ".join(string_list)
print(my_output)
