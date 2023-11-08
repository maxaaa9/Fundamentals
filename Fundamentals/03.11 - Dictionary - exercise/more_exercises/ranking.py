data_contest = {}
while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    data_contest[contest] = password

user_dictionary = {}
while True:
    input_data = input()
    if input_data == "end of submissions":
        break
    contest, password, username, points = input_data.split("=>")
    points = int(points)
    if contest in data_contest.keys():
        if password == data_contest[contest]:
            if username not in user_dictionary.keys():
                user_dictionary[username] = {}
            user_dictionary[username].update({contest: points})
            if contest in user_dictionary[username]:
                if user_dictionary[username][contest] < points:
                    user_dictionary[username][contest] = points

best_candidate = ""
my_sorted_list = list(user_dictionary.keys())
my_sorted_list.sort()
sorted_dictionary = {i: user_dictionary[i] for i in my_sorted_list}
# print(f"Best candidate is {user} with total {total_points} points.")
for user in sorted_dictionary.keys():
    print(user)
    for module, score in sorted_dictionary[user].items():
        print(f"{module} -> {score}")
