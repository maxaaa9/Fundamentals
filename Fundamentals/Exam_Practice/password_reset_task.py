# Write a password reset program that performs a series of commands upon a predefined string.
#   First, you will receive a string, and afterward, until the command "Done" is given,
#       you will be receiving strings with commands split by a single space. The commands will be the following:
# "TakeOdd"
#  Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# "Cut {index} {length}"
# Gets the substring with the given length starting from the given index
#   from the password and removes its first occurrence, then prints the password on the console.
# The given index and the length will always be valid.
# "Substitute {substring} {substitute}"
# If the raw password contains the given substring,
#   replace all of its occurrences with the substitute text given and print the result.
# If it doesn't, prints "Nothing to replace!".


def take_odd(check_string: str) -> str:
    new_password = ""
    for odd_indices in range(len(check_string)):
        if odd_indices % 2 != 0:
            new_password += check_string[odd_indices]
    return new_password


def cut(from_len, indices, string) -> str:
    new_string = string[:from_len] + string[from_len + indices:]
    return new_string


raw_password = input()

while True:
    command = input().split()
    if command[0] == "Done":
        print(f"Your password is: {raw_password}")
        break

    if command[0] == "TakeOdd":
        raw_password = take_odd(raw_password)
        print(raw_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = cut(index, length, raw_password)
        print(raw_password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

