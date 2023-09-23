number_of_lines = int(input())

bracket_checker = ""
balanced = False

for i in range(number_of_lines):
    insert = input()
    if insert == "(":
        bracket_checker += insert
    elif insert == ")":
        bracket_checker += insert
    if bracket_checker == "()":
        bracket_checker = ""
        balanced = True
if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
