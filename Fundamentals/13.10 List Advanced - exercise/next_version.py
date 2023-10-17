def version_validator(sequence: list) -> str:
    for three in range(1):
        sequence[2] += 1
        if sequence[2] > 9:
            sequence[2] = 0
            sequence[1] += 1
    for two in range(1):
        if sequence[1] > 9:
            sequence[1] = 0
            sequence[0] += 1

    return ".".join(str(s) for s in sequence)


sequence_of_numbers = list(map(int, input().split(".")))

print(version_validator(sequence_of_numbers))
