sequence_of_nums = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "end":
        print(", ".join(map(str, sequence_of_nums)))
        break
    if len(command) > 1:
        index_one = int(command[1])
        index_two = int(command[2])
    if command[0] == "swap":
        sequence_of_nums[index_one], sequence_of_nums[index_two] \
            = sequence_of_nums[index_two], sequence_of_nums[index_one]
    elif command[0] == "multiply":
        sequence_of_nums[index_one] = sequence_of_nums[index_one] * sequence_of_nums[index_two]
    elif command[0] == "decrease":
        sequence_of_nums = [x - 1 for x in sequence_of_nums]
