# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
#   Every odd line on the console represents a resource
#   (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
#   Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

resource_list = []
while True:
    command = input()
    if command == "stop":
        break
    resource_list.append(command)

resource_dictionary = {}
for num in range(0, len(resource_list), 2):
    if resource_list[num] not in resource_dictionary.keys():
        resource_dictionary[resource_list[num]] = int(resource_list[num + 1])
    else:
        resource_dictionary[resource_list[num]] += int(resource_list[num + 1])

for resource, quantity in resource_dictionary.items():
    print(f"{resource} -> {quantity}")
