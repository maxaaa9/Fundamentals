import re


text = input()
daily_income = 0
while text != "end of shift":
    pattern = r"\%([A-Z][a-z]+)\%[^|,$,\%\.]*\<(\w+)\>[^|,$,\%\.]*\|(\d+)\|[^|,$,\%\.]*?(\d+\.?\d+?)\$"
    validator = re.findall(pattern, text)
    if validator:
        name = validator[0][0]
        product = validator[0][1]
        quantity = int(validator[0][2])
        price = float(validator[0][3])
        total_price = quantity * price
        daily_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")
    text = input()

print(f"Total income: {daily_income:.2f}")
