key_value = input().split()
search_product = input().split()

my_dict = {}

for i in range(0, len(key_value), 2):
    key = key_value[i]
    value = int(key_value[i + 1])
    my_dict[key] = value

for product in search_product:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
