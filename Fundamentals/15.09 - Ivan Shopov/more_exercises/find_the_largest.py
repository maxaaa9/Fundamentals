number = input()

largest_number = sorted(number, reverse=True)
largest_number = int("".join(largest_number))
print(int(largest_number))
