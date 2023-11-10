dictionary = {}
statistical_dictionary = {}
while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)
    if username not in dictionary.keys():
        dictionary[username] = {contest: points}

    if username not in statistical_dictionary.keys():
        statistical_dictionary[username] = points
    if points > statistical_dictionary[username] and contest in dictionary[username]:
        statistical_dictionary[username] = points
    if contest not in dictionary[username]:
        dictionary[username].update({contest: points})
    if contest in dictionary[username]:
        if points > dictionary[username][contest]:
            dictionary[username][contest] = points

courses_count_dict = {}
for dict_value in dictionary.values():
    for course in dict_value.keys():
        if course not in courses_count_dict:
            courses_count_dict[course] = 0
        courses_count_dict[course] += 1

dictionary = dict(sorted(dictionary.items(), key=lambda x: next(iter(x[1].values()), 0), reverse=True))

for contest_course, participants in courses_count_dict.items():
    print(f"{contest_course}: {participants} participants")
    participant_counter = 1
    for check_username in dictionary.keys():
        if contest_course in dictionary[check_username].keys():
            print(f"{participant_counter}. {check_username} <::> {dictionary[check_username][contest_course]}")
            participant_counter += 1

statistical_dictionary = dict(sorted(statistical_dictionary.items(), key=lambda x: -x[1]))
print("Individual standings:")
counter = 1
for username, scores in statistical_dictionary.items():
    print(f"{counter}. {username} -> {scores}")
    counter += 1
