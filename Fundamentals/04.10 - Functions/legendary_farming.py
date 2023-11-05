# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However,
#   it's a tedious process, and it requires quite a bit of farming. The possible items are:
# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
#   At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.


material_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
obtained = ""
while obtained == "":
    material = input().split()
    for check in range(1, len(material), 2):
        material[check] = material[check].lower()
        if material[check] not in material_dictionary:
            material_dictionary[material[check]] = int(material[check - 1])
        else:
            material_dictionary[material[check]] += int(material[check - 1])
        if material_dictionary["fragments"] >= 250:
            material_dictionary["fragments"] -= 250
            obtained = "Valanyr"

        elif material_dictionary["shards"] >= 250:
            material_dictionary["shards"] -= 250
            obtained = "Shadowmourne"

        elif material_dictionary["motes"] >= 250:
            material_dictionary["motes"] -= 250
            obtained = "Dragonwrath"

        if obtained != "":
            break

print(f"{obtained} obtained!")
for element, value in material_dictionary.items():
    print(f"{element}: {value}")
