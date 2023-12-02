def move(message, num_letters):
    message = message[num_letters:] + message[:num_letters]
    return message


def insert(message, insert_index, insert_value):
    message = message[:insert_index] + insert_value + message[insert_index:]
    return message


def change_all(text, substring, replace):
    text = text.replace(substring, replace)
    return text


encrypted_message = input()

while True:
    command = input().split("|")

    if command[0] == "Decode":
        break

    if command[0] == "Move":
        number_of_letters = int(command[1])
        encrypted_message = move(encrypted_message, number_of_letters)

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = insert(encrypted_message, index, value)

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)

print(f"The decrypted message is: {encrypted_message}")