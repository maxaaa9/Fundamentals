# Write a program that processes information about a race.
#   On the first line you will be given list of participants separated by ", ".
#   On the next few lines until you receive a line "end of race"
#       you will be given some info which will be some alphanumeric characters.
#       In between them you could have some extra characters which you should ignore.
#       For example: "G!32e%o7r#32g$235@!2e".
#       The letters are the name of the person and the sum of the digits is the distance he ran.
#       So here we have George who ran 29 km.
#       Store the information about the person only if the list of racers contains the name of the person.
#       If you receive the same person more than once just add the distance to his old distance.
#       At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"


import re

list_of_participants = [x for x in input().split(", ")]

name_pattern = r"[A-Za-z]"
digit_pattern = r"\d"
ranking_dictionary = {}
while True:
    command = input()

    if command == "end of race":
        break
    check_participant = "".join(re.findall(name_pattern, command))
    if check_participant in list_of_participants:
        digit = sum(int(x) for x in re.findall(digit_pattern, command))
        if check_participant not in ranking_dictionary.keys():
            ranking_dictionary[check_participant] = digit
        else:
            ranking_dictionary[check_participant] += digit
sorted_list = sorted(ranking_dictionary.items(), key=lambda x: -x[1])
for name in range(3):
    if name == 0:
        print(f"{name + 1}st place: {sorted_list[name][0]}")
    elif name == 1:
        print(f"{name + 1}nd place: {sorted_list[name][0]}")
    elif name == 2:
        print(f"{name + 1}rd place: {sorted_list[name][0]}")
