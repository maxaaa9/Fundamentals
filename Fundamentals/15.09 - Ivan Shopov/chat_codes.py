number_massages = int(input())

for send in range(number_massages):
    text = ""
    code = int(input())
    if code == 88:
        text = "Hello"

    elif code == 86:
        text = "How are you?"

    elif code < 88:
        text = "GREAT!"

    else:
        text = "Bye."
    print(text)
