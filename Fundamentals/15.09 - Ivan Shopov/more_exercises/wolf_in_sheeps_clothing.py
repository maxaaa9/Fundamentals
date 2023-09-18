word = input()

result = word.split(", ")[::-1]
x = len(result)

wolf_position = result.index("wolf")

if result[0] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")



