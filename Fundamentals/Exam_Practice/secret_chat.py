concealed_message = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        break

    if command[0] == "InsertSpace":
        my_index = int(command[1])
        concealed_message = concealed_message[:my_index] + " " + concealed_message[my_index:]

    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
        else:
            print("error")

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)
print(f"You have a new text message: {concealed_message}")