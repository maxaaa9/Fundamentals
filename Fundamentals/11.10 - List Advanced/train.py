def wagon_length(numbers):
    wagon_list = []
    for wagon in range(0, numbers):
        wagon_list.append(0)
    return wagon_list


number_of_wagons = int(input())
my_wagon_list = wagon_length(number_of_wagons)
while True:
    command = input().split()
    if command[0] == "End":
        print(my_wagon_list)
        break

    elif command[0] == "add":
        number_of_people = int(command[1])
        my_wagon_list[-1] += number_of_people
    elif "insert" in command:
        index = int(command[1])
        number_of_people = int(command[2])
        my_wagon_list[index] += number_of_people
    elif "leave" in command:
        index = int(command[1])
        people = int(command[2])
        my_wagon_list[index] -= people


