first_row = input().split()
second_row = input().split()
third_row = input().split()

first_row = "".join(first_row)
second_row = "".join(second_row)
third_row = "".join(third_row)

first_column = first_row[0] + second_row[0] + third_row[0]
second_column = first_row[1] + second_row[1] + third_row[1]
third_column = first_row[2] + second_row[2] + third_row[2]

first_diagonal = first_column[0] + second_column[1] + third_column[2]
second_diagonal = first_column[2] + second_column[1] + third_column[0]

my_full_list = [first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal, second_diagonal]
winner = ""
if "111" in my_full_list:
    winner = "First"
elif "222" in my_full_list:
    winner = "Second"

if winner != "":
    print(f"{winner} player won")
else:
    print("Draw!")
