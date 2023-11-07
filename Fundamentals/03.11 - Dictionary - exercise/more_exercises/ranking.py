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
    if command == "end of submissions":
        break
    contest, password, username, points = input_data.split("=>")
    points = int(points)
    if contest in data_contest.keys():
        if password == data_contest[contest]:
            if username not in user_dictionary.keys():
                user_dictionary[username] = {}
            user_dictionary[username].update({contest: points})
            if contest in user_dictionary.values():
                if user_dictionary.values() < points:
                    user_dictionary[contest].values()
