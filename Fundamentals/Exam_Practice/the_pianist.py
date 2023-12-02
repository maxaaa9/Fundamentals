def add_element(dictionary, pieces, composers, keys) -> dict:
    dictionary[pieces] = {"composer": composers, "key": keys}
    return dictionary


number_of_pieces = int(input())

pieces_dict = {}
for _ in range(number_of_pieces):
    pieces_themself = input().split("|")
    piece = pieces_themself[0]
    composer = pieces_themself[1]
    key = pieces_themself[2]
    pieces_dict = add_element(pieces_dict, piece, composer, key)

while True:
    command = input().split("|")

    if command[0] == "Stop":
        break
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
            continue
        pieces_dict = add_element(pieces_dict, piece, composer, key)
        print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == "Remove":
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
            continue
        print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        new_key = command[2]
        if piece in pieces_dict.keys():
            pieces_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for pcs in pieces_dict.keys():
    print(f"{pcs} -> Composer: {pieces_dict[pcs]['composer']}, Key: {pieces_dict[pcs]['key']}")
