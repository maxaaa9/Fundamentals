number = int(input())
sorted_digits = sorted(str(number), reverse=True)
largest_number = int(''.join(sorted_digits))
print(largest_number)
