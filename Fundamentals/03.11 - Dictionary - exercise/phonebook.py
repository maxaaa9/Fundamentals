# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
#   If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
#   Your program should be able to perform a search of contact by name and print its details in the format:
#   "{name} -> {number}". In case the contact isn't found, print: "Contact {name} does not exist."

phonebook_dictionary = {}
phonebook_counter = 0
while True:
    command = input()
    if command.isdigit():
        phonebook_counter = int(command)
        break
    name, phone_number = command.split("-")
    phonebook_dictionary[name] = phone_number

for check_name in range(phonebook_counter):
    contact_name = input()
    if contact_name in phonebook_dictionary.keys():
        print(f"{contact_name} -> {phonebook_dictionary[contact_name]}")
        continue
    print(f"Contact {contact_name} does not exist.")
