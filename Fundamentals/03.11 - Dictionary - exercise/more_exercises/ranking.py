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
                user_dictionary[username] = {contest: points}
            if contest not in user_dictionary[username]:
                user_dictionary[username].update({contest: points})
            if points > user_dictionary[username][contest]:
                user_dictionary[username].update({contest: points})

best_candidate = {}
for candidate in user_dictionary.keys():
    for course, score_sum in user_dictionary[candidate].items():
        if candidate not in best_candidate.keys():
            best_candidate[candidate] = 0
        best_candidate[candidate] += score_sum
sorted_dictionary = {key: dict(sorted(val.items(), key=lambda x: -x[1])) for key, val in user_dictionary.items()}
sorted_dictionary = dict(sorted(sorted_dictionary.items()))
print(f"Best candidate is {max(best_candidate)} with total {best_candidate[max(best_candidate)]} points.\nRanking:")
for user in sorted_dictionary.keys():
    print(user)
    for module, score in sorted_dictionary[user].items():
        print(f"#  {module} -> {score}")
