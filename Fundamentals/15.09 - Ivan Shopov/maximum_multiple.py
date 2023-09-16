divisor = int(input())
boundary = int(input())

for output in range(boundary, divisor, -1):
    if output % divisor == 0:
        print(output)
        break
