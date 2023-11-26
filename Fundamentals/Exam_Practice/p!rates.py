def plunder(cities_dict, village, peoples,  money) -> dict:
    cities_dict[village]["Population"] -= peoples
    cities_dict[village]["Gold"] -= money
    print(f"{village} plundered! {money} gold stolen, {peoples} citizens killed.")
    if cities_dict[village]["Population"] == 0 or cities_dict[village]["Gold"] == 0:
        cities_dict.pop(village)
        print(f"{village} has been wiped off the map!")
    return cities_dict


def prosper(cities_dict, village, coins) -> dict:
    cities_dict[village]["Gold"] += coins
    total_gold = cities_dict[village]["Gold"]
    print(f"{coins} gold added to the city treasury. {village} now has {total_gold} gold.")
    return cities_dict


cities = {}
while True:
    command = input().split("||")

    if command[0] == "Sail":
        break

    city = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city not in cities.keys():
        cities[city] = {"Population": 0, "Gold": 0}

    cities[city]["Population"] += population
    cities[city]["Gold"] += gold

while True:
    event = input().split("=>")
    if event[0] == "End":
        break

    if event[0] == "Plunder":
        town = event[1]
        people = int(event[2])
        plunder_gold = int(event[3])
        cities = plunder(cities, town, people, plunder_gold)

    elif event[0] == "Prosper":
        prosper_town = event[1]
        prosper_gold = int(event[2])
        if prosper_gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities = prosper(cities, prosper_town, prosper_gold)

if cities:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    for towns in cities.keys():
        print(f"{towns} -> Population: {cities[towns]['Population']} citizens, Gold: {cities[towns]['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
