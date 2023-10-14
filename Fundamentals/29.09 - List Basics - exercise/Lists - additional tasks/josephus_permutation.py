people_in_list = input().split()
number = int(input())

my_execute_list = []
member = 0
while len(people_in_list) != 0:
    member = (member + number - 1) % len(people_in_list)
    my_execute_list.append(people_in_list.pop(member))
my_integer_list = [str(integer) for integer in my_execute_list]
my_integer_list = f"[{','.join(my_integer_list)}]"
print(my_integer_list)
