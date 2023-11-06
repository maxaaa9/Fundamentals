# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users.
#   For each course, print the registered users.
# Input
# Until the "end" command is received, you will be receiving input lines in the format:
# "{course_name} : {student_name}"
# The product data is always delimited by " : "


student_dictionary = {}
while True:
    command = input()
    if command == "end":
        break
    course, student = command.split(" : ")
    if course not in student_dictionary.keys():
        student_dictionary[course] = []
    if student not in student_dictionary[course]:
        student_dictionary[course].append(student)

for course_name, members in student_dictionary.items():
    print(f"{course_name}: {len(members)}")
    for student_names in members:
        print(f"-- {student_names}")
