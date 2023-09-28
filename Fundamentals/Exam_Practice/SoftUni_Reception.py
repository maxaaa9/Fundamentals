from math import ceil
first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_students = int(input())
total_capacity_of_employee = first_employee + second_employee + third_employee
hours_counter = 0
while total_students > 0:
    total_students -= total_capacity_of_employee
    hours_counter += 1
    if hours_counter % 4 == 0:
        hours_counter += 1

print(f"Time needed: {hours_counter}h.")
