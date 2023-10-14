waiting_peoples = int(input())
lift_state = input().split()
lift_state = [int(x) for x in lift_state]
for check in range(len(lift_state)):
    while lift_state[check] < 4 and waiting_peoples > 0:
        lift_state[check] += 1
        waiting_peoples -= 1
free_spots = len(lift_state) * 4 - sum(lift_state)
lift_state = " ".join(map(str, lift_state))

if waiting_peoples == 0 and free_spots == 0:
    print(lift_state)
elif waiting_peoples > 0 and free_spots == 0:
    print(f"There isn't enough space! {waiting_peoples} people in a queue!\n{lift_state}")

else:
    print(f"The lift has empty spots!\n{lift_state}")
