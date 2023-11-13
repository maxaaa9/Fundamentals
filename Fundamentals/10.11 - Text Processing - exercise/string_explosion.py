# Write a program that reads a string from the console that contains:
# Explosions marked with '>'
# Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# Any other characters
# Your task is to delete x characters, starting after the exploded character ('>').
#   If you find another explosion mark ('>') while deleting characters,
#       you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.

started_string = input()
sequence_of_string = started_string
new_string = ""
strength_of_explosion = 0
for check_index in range(len(sequence_of_string)):
    if sequence_of_string[check_index] != ">" and strength_of_explosion > 0:
        strength_of_explosion -= 1
    elif sequence_of_string[check_index] != ">" and strength_of_explosion <= 0:
        new_string += sequence_of_string[check_index]
    elif sequence_of_string[check_index] == ">":
        new_string += sequence_of_string[check_index]
        boom_sum = ""
        for check_digit in range(check_index, len(sequence_of_string) - 1):
            if sequence_of_string[check_digit + 1].isdigit():
                boom_sum += sequence_of_string[check_digit + 1]
            else:
                strength_of_explosion += int(boom_sum)
                break

print(new_string)
