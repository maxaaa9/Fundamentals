from math import ceil
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_students = int(input())

total_capacity_of_employee = first_employee + second_employee + third_employee
needed_hour = total_students / total_capacity_of_employee
needed_hour = ceil(needed_hour)
needed_hour += needed_hour // 4
print(f"Time needed: {needed_hour}h.")
