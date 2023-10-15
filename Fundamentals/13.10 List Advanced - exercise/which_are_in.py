def substring_in_list(substrings, list_with_strings: list) -> list:
    output_list = []
    for sub in substrings:
        for string in list_with_strings:
            if sub in string:
                output_list.append(sub)
                break

    return output_list


substring = input().split(", ")
strings = input().split(", ")
result = substring_in_list(substring, strings)
print(result)