sequence_of_nums = list(map(int, input().split()))

average_sum = sum(sequence_of_nums) / len(sequence_of_nums)
my_output = sorted(list(x for x in sequence_of_nums if x > average_sum), reverse=True)
five_elements = []
for five in my_output:
    if len(five_elements) < 5:
        five_elements.append(str(five))
five_elements = " ".join(five_elements)
if len(five_elements) == 0:
    print("No")
else:
    print(five_elements)
