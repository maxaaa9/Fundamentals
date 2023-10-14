sum_without_taxes = 0
sum_with_taxes = 0
break_time = False
special_client = False
while True:
    command = input()
    if command == "regular" or command == "special":
        if command == "special":
            special_client = True
        break_time = True
        break
    if not command.isalpha():
        command = float(command)
        if command < 0:
            print("Invalid price!")
            continue
        else:
            sum_without_taxes += command
            sum_with_taxes += command * 1.2

if sum_without_taxes == 0:
    print("Invalid order!")
elif break_time:
    final_sum = sum_with_taxes
    if special_client:
        final_sum *= 0.9
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {sum_without_taxes:.2f}$\n"
          f"Taxes: {sum_with_taxes - sum_without_taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_sum:.2f}$")
    