int_one = int(input())
int_two = int(input())
int_three = int(input())

count = 0

if int_one < 0:
    count += 1
if int_two < 0:
    count += 1
if int_three < 0:
    count += 1

if int_one == 0 or int_two == 0 or int_three == 0:
    print("zero")
elif count % 2 == 1:
    print("negative")
else:
    print("positive")

