my_input = input().split("|")
energy = 100
coin = 100
handle_all_events = True
for i in my_input:
    splitter = i.split("-")
    event = splitter[0]
    number = int(splitter[1])
    if event == "rest":
        current_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            energy -= 30
            coin += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coin >= number:
            coin -= number
            print(f"You bought {event}.")
        else:
            handle_all_events = False
            break

if handle_all_events:
    print("Day completed!")
    print(f"Coins: {coin}")
    print(f"Energy: {energy}")
else:
    print(f"Closed! Cannot afford {event}.")
