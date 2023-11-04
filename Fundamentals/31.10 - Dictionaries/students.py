students_dictionary = {}
while True:
    students = input()
    if ":" not in students:
        for key, value in students_dictionary.items():
            value = value.split(":")
            if students.startswith(value[1][0:5]):
                print(f"{value[0]} - {key}")
        break
    name, number, course = students.split(":")
    students_dictionary[number] = name + ":" + course
