number_of_rooms = int(input())
free_chairs = 0
print_chairs = True
for room in range(number_of_rooms):
    room_check = input().split()
    visitors = int(room_check[1])
    sum_of_chairs = len(room_check[0])
    difference = sum_of_chairs - visitors
    if difference >= 0:
        free_chairs += difference
    else:
        print(f"{abs(difference)} more chairs needed in room {room + 1}")
        print_chairs = False
if print_chairs:
    print(f"Game On, {free_chairs} free chairs left")
