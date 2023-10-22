def index_validator(my_list, first_index, second_index) -> bool:
    statement = True
    if first_index == second_index:
        statement = False
    if 0 > first_index or 0 > second_index:
        statement = False
    if first_index > len(my_list) - 1 or second_index > len(my_list) - 1:
        statement = False
    return statement


sequence_of_nums = [x for x in input().split()]
turns = 0
while True:
    command = input().split()
    if command[0] == "end" and len(sequence_of_nums) > 1:
        print(f'Sorry you lose :(\n{" ".join(sequence_of_nums)}')
        break
    turns += 1
    middle_of_list = len(sequence_of_nums) // 2
    if len(command) > 1:
        if not index_validator(sequence_of_nums, int(command[0]), int(command[1])):
            sequence_of_nums.insert(middle_of_list, str(f"-{turns}a"))
            sequence_of_nums.insert(middle_of_list, str(f"-{turns}a"))
            print(f"Invalid input! Adding additional elements to the board")

        elif sequence_of_nums[int(command[0])] == sequence_of_nums[int(command[1])]:
            index_one = sequence_of_nums[int(command[0])]
            index_two = sequence_of_nums[int(command[1])]
            sequence_of_nums.remove(index_one)
            sequence_of_nums.remove(index_two)
            print(f"Congrats! You have found matching elements - {index_one}!")

        elif sequence_of_nums[int(command[0])] != sequence_of_nums[int(command[1])]:
            print("Try again!")

    if len(sequence_of_nums) == 0:
        print(f"You have won in {turns} turns!")
        break
