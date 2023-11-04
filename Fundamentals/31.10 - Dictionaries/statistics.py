key_values = {}
while True:
    command = input()
    if command == "statistics":
        print("Products in stock:")
        for keys, values in key_values.items():
            print(f"- {keys}: {values}")
        print(f"Total Products: {len(key_values.keys())}")
        print(f"Total Quantity: {sum(key_values.values())}")
        break

    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in key_values:
        key_values[key] = value
    else:
        key_values[key] += value

