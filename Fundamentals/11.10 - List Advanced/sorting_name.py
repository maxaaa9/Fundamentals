def sort_names(string_word) -> list:
    sorted_list = sorted(string_word.split(", "), key=lambda x: (-len(x), x))

    return sorted_list


my_words = input()
result = sort_names(my_words)
print(result)
