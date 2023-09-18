word = input()

my_list = []

for index, char in enumerate(word):
    if char.isupper():
        my_list.append(index)

print(my_list)