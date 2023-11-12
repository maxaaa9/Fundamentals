# Create a program that receives two strings on a single line separated by a single space.
#   Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0]
#       and add the result to the total sum, then continue with the next two characters.
#       If one of the strings is longer than the other,
#           add the remaining character codes to the total sum without multiplication.


one, two = input().split()
total_sum = 0
shorter_string = two if len(two) < len(one) else one
longer_string = two if len(two) >= len(one) else one
for symbol in range(len(shorter_string)):
    total_sum += ord(one[symbol]) * ord(two[symbol])
if len(shorter_string) != len(longer_string):
    for add_sum in range(len(shorter_string), len(longer_string)):
        total_sum += ord(longer_string[add_sum])

print(total_sum)
