import re
barcode_count = int(input())
pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
for check_barcodes in range(barcode_count):
    barcode = input()
    valid_pattern = re.findall(pattern, barcode)
    if len(valid_pattern) == 0:
        print("Invalid barcode")
        continue
    group = "00"
    valid_pattern = str(valid_pattern[0][1])
    for check_digit in valid_pattern:
        if check_digit.isdigit():
            if group == "00":
                group = ""
            group += check_digit
    print(f'Product group: {group}')
