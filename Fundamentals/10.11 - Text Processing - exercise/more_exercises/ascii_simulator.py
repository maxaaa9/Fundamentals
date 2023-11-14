# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
#   On each of the first two lines, you will receive a single character.
#       On the last line, you get a random string.
#           Print the sum of the ASCII values of all characters in the random string
#               between the two given characters in the ASCII table.
char_one = ord(input())
char_two = ord(input())
text = input()

total_sum = 0
for ord_check in text:
    if char_one < ord(ord_check) < char_two:
        total_sum += ord(ord_check)

print(total_sum)
