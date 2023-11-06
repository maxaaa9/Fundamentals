# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
#   On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students
#   with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

pairs = int(input())
students_grade_dictionary = {}
for _ in range(pairs):
    student = input()
    grade = float(input())
    if student not in students_grade_dictionary.keys():
        students_grade_dictionary[student] = []
    students_grade_dictionary[student].append(grade)

for students, grade_list in students_grade_dictionary.items():
    average_grade = sum(grade_list) / len(grade_list)
    if average_grade >= 4.50:
        print(f"{students} -> {average_grade:.2f}")