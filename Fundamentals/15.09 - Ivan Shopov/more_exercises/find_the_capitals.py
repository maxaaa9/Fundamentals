word = input()

my_list = []

for index, i in enumerate(word):
    if i.isupper():
        my_list.append(index)

print(my_list)



