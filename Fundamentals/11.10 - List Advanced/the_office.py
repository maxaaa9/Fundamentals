def happiness_factor(happiness_list, amplify) -> list:
    happiness_list = list(map(int, happiness_list))
    amp_list = list(x * amplify for x in happiness_list)
    happiness_list = filter(lambda x: x > (sum(amp_list)) // len(amp_list), amp_list)
    return list(happiness_list)


all_employees_evaluation = input().split()
improvement_factor = int(input())
happy_employees = happiness_factor(all_employees_evaluation, improvement_factor)
if len(happy_employees) >= len(all_employees_evaluation) // 2:
    happy_note = "happy"
else:
    happy_note = "not happy"
print(f"Score: {len(happy_employees)}/{len(all_employees_evaluation)}. Employees are {happy_note}!")
