sequence_of_coffee = input().split()

commands = int(input())
for i in range(commands):
    command = input().split()
    if command[0] == "Include":
        coffee = command[1]
        sequence_of_coffee.append(coffee)
    elif command[0] == "Remove":
        first_last = command[1]
        number_of_coffees = int(command[2])
        if len(sequence_of_coffee) < number_of_coffees:
            continue
        if first_last == "first":
            for remover in range(number_of_coffees):
                sequence_of_coffee.remove(sequence_of_coffee[0])
        elif first_last == "last":
            for remove_last in range(number_of_coffees):
                sequence_of_coffee.pop()
    elif command[0] == "Prefer":
        coffee_index_one = int(command[1])
        coffee_index_two = int(command[2])
        if len(sequence_of_coffee) - 1 < coffee_index_one and len(sequence_of_coffee) - 1 < coffee_index_two:
            continue
        else:
            sequence_of_coffee[coffee_index_one], sequence_of_coffee[coffee_index_two] \
                = sequence_of_coffee[coffee_index_two], sequence_of_coffee[coffee_index_one]
    elif command[0] == "Reverse":
        sequence_of_coffee.reverse()

print(f"Coffees:\n{' '.join(sequence_of_coffee)}")
