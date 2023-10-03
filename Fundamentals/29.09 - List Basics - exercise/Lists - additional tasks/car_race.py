sequence_of_numbers = input().split()

middle_index = len(sequence_of_numbers) // 2

left_car = sequence_of_numbers[:middle_index]
right_car = sequence_of_numbers[middle_index + 1:]
right_car.reverse()

left_car_timer = 0
right_car_timer = 0
for left in left_car:
    left = int(left)
    if left != 0:
        left_car_timer += left
    else:
        left_car_timer *= 0.8
for right in right_car:
    right = int(right)
    if right != 0:
        right_car_timer += right
    else:
        right_car_timer *= 0.8

if left_car_timer < right_car_timer:
    print(f"The winner is left with total time: {left_car_timer:.1f}")
else:
    print(f"The winner is right with total time: {right_car_timer:.1f}")