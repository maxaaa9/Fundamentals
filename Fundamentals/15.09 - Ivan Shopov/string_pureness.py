number = int(input())

for i in range(number):
    pureness = True
    word = input()
    if "," in word \
            or "." in word\
            or "_" in word:
        pureness = False

    if pureness:
        print(f"{word} is pure.")
    else:
        print(f"{word} is not pure!")
