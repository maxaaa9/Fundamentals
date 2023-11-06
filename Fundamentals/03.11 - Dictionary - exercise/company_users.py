# You will be receiving company names and an employees' id until you receive the command "End" command.
#   Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
# Print the company name and each employee's id in the following format:
# "{company_name}
# -- {id1}
# -- {id2}
# …
# -- {idN}"


users_dictionary = {}
while True:
    command = input()
    if command == "End":
        break
    company, employees_id = command.split(" -> ")
    if company not in users_dictionary.keys():
        users_dictionary[company] = [employees_id]
    if employees_id not in users_dictionary[company]:
        users_dictionary[company].append(employees_id)

for company_name, employees_number in users_dictionary.items():
    print(f"{company_name}")
    for ID in employees_number:
        print(f"-- {ID}")
