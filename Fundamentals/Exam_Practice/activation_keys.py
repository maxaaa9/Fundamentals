def contains(key, string) -> print:
    if string in key:
        return print(f"{key} contains {string}")
    return print("Substring not found!")


def flipper(key, up_low_case, start_idx, end_idx) -> str:
    key_substring = key[start_idx:end_idx].lower() if up_low_case == "Lower" else key[start_idx:end_idx].upper()
    new_key = key[:start_idx] + key_substring + key[end_idx:len(key)]
    print(new_key)
    return new_key


def slicer(key, start_slice, end_slice) -> str:
    key = key[:start_slice] + key[end_slice:]
    print(key)
    return key


activation_key = input()

while True:
    command = input().split(">>>")

    if command[0] == "Generate":
        break

    if command[0] == "Contains":
        substring = command[1]
        contains(activation_key, substring)

    elif command[0] == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        activation_key = flipper(activation_key, case, start_index, end_index)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = slicer(activation_key, start_index, end_index)

print(f"Your activation key is: {activation_key}")
