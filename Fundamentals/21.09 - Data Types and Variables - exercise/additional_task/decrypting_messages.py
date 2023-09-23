key = int(input())
number = int(input())
decrypted_message = ""
for i in range(number):
    symbol = input()
    symbol = ord(symbol) + key
    symbol = chr(symbol)
    decrypted_message += symbol

print(decrypted_message)
