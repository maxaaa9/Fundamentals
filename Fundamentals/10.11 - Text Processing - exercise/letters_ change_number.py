# You receive a string consisting of a number between two letters.
#   For the given string, you should perform different mathematical operations to achieve a result:
# First, if the letter in front of the number is:
# Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# Next, if the letter after the number is:
# Uppercase: subtract its position from the resulting number (starting from 1)
# Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings
#   keeping track of only the total sum of all results.
#       Once he started to solve this with more strings and bigger numbers,
#           it became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations
#   described above and sums the final results of each string.


def alphabet_order(char: str) -> int:
    char = ord(char.lower()) - 96
    return char


input_string = input().split()

total_sum = 0
for check_word in input_string:
    first_char = check_word[0]
    last_char = check_word[-1]
    digits = int(check_word[1:-1])
    if first_char.isupper():
        digits /= alphabet_order(first_char)
    else:
        digits *= alphabet_order(first_char)

    if last_char.isupper():
        digits -= alphabet_order(last_char)
    else:
        digits += alphabet_order(last_char)
    total_sum += float(digits)

print(f"{total_sum:.2f}")
