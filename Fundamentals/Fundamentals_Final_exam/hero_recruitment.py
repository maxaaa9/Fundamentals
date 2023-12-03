hero_collection = {}

while True:
    command = input().split()

    if command[0] == "End":
        break

    hero_name = command[1]
    if command[0] == "Enroll":
        if hero_name in hero_collection.keys():
            print(f"{hero_name} is already enrolled.")
            continue
        hero_collection[hero_name] = []

    elif command[0] == "Learn":
        spell_name = command[2]
        if hero_name not in hero_collection:
            print(f"{hero_name} doesn't exist.")
            continue
        if spell_name in hero_collection[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
            continue
        hero_collection[hero_name].append(spell_name)
    elif command[0] == "Unlearn":
        unlearn = command[2]
        if hero_name not in hero_collection.keys():
            print(f"{hero_name} doesn't exist.")
            continue
        if unlearn in hero_collection[hero_name]:
            hero_collection[hero_name].remove(unlearn)
        else:
            print(f"{hero_name} doesn't know {unlearn}.")

print("Heroes:")

for hero in hero_collection.keys():
    hero_spell_list = ", ".join(hero_collection[hero])
    print(f"== {hero}: {hero_spell_list}")
