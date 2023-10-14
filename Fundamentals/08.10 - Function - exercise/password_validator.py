def password_validator(my_password: str) -> list:
    list_of_errors = []
    if not 6 <= len(my_password) <= 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not my_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for check in my_password:
        if check.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")

    return list_of_errors


my_password = input()
valid_password = password_validator(my_password)
if len(valid_password) == 0:
    print("Password is valid")
else:
    print("\n".join(valid_password))
