def symbol_printer_in_ASCII_range(started_char, ended_char) -> str:
    my_string = ""
    for char in range(ord(started_char) + 1, ord(ended_char)):
        my_string += chr(char)
    print(" ".join(my_string))
    return my_string


character_one = input()
character_two = input()
symbol_printer_in_ASCII_range(character_one, character_two)
