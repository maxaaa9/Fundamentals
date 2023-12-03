my_string = input()

while True:
    command = input().split()

    if command[0] == "Done":
        break

    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        my_string = my_string.replace(char, replacement)
        print(my_string)

    elif command[0] == "Includes":
        substring = command[1]
        if substring in my_string:
            print("True")
            continue
        print("False")
    elif command[0] == "End":
        end_substring = command[1]
        if my_string.endswith(end_substring):
            print("True")
            continue
        print("False")
    elif command[0] == "Uppercase":
        my_string = "".join(str(x) for x in my_string.upper())
        print(my_string)

    elif command[0] == "FindIndex":
        find_char = command[1]
        find_index = my_string.index(find_char)
        print(find_index)

    elif command[0] == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        cut_chars = my_string[start_index:start_index+count]
        print(cut_chars)