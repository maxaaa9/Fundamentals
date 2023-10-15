def even_list(my_string: str) -> list:
    my_string = list(map(int, my_string.split(", ")))
    my_string = list(filter(lambda x: my_string[x] % 2 == 0, range(len(my_string))))
    return my_string


words = input()
result = even_list(words)
print(result)
