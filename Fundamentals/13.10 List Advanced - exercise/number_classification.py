sequence_of_nums = input().split(", ")

positive_list = ", ".join(x for x in sequence_of_nums if int(x) >= 0)
negative_list = ", ".join(x for x in sequence_of_nums if int(x) < 0)
even_list = ", ".join(x for x in sequence_of_nums if int(x) % 2 == 0)
odd_list = ", ".join(x for x in sequence_of_nums if int(x) % 2 != 0)

print(f"Positive: {positive_list}")
print(f"Negative: {negative_list}")
print(f"Even: {even_list}")
print(f"Odd: {odd_list}")
