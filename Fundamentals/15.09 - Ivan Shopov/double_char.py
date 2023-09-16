word = input()
while word != "End":
    if word != "SoftUni":
        for index in range(len(word)):
            print(word[index] * 2, end="")
        print()
    word = input()

