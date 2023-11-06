students_dictionary = {}
submission_dictionary = {}
while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    name = command[0]
    course = command[1]
    if course == "banned" and name in students_dictionary.keys():
        students_dictionary.pop(name)
        continue
    score = int(command[2])
    if course not in submission_dictionary.keys():
        submission_dictionary[course] = 0
    submission_dictionary[course] += 1
    if name not in students_dictionary.keys():
        students_dictionary[name] = []
    students_dictionary[name].append(score)

print("Results:")
for student, score in students_dictionary.items():
    print(f"{student} | {max(score)}")

print("Submissions:")
for courses, count in submission_dictionary.items():
    print(f"{courses} - {count}")
