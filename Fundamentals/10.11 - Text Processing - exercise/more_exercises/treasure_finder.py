# Write a program that decrypts a message by a given key
#   and gathers information about hidden treasure type and its coordinates.
#   On the first line, you will receive a key (sequence of numbers separated by a space).
#   On the next few lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number
#   of the key sequence. You choose a key number from the sequence by just looping through it.
#       If the length of the key sequence is less than the string sequence,
#           you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates.
#   The type will be between the symbol "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".

key = input().split()

decrypted_word = ""
while True:
    command = input()
    if command == "find":
        break
    key_index = 0
    for each in command:
        decrypted_word += chr(ord(each) - int(key[key_index]))
        key_index += 1
        if key_index == len(key):
            key_index = 0
    treasure_type = ""
    for type_treasure in decrypted_word:
        if type_treasure == "&":
            treasure_type = decrypted_word[decrypted_word.index(type_treasure) + 1:]
            for end in treasure_type:
                if end == "&":
                    treasure_type = treasure_type[:treasure_type.index(end)]
                    break
    coordinates = ""
    for coordinate in decrypted_word:
        if coordinate == "<":
            coordinates = decrypted_word[decrypted_word.index(coordinate) + 1:]
        elif coordinate == ">":
            coordinates = coordinates[:coordinates.index(coordinate)]

    decrypted_word = ""
    print(f"Found {treasure_type} at {coordinates}")
