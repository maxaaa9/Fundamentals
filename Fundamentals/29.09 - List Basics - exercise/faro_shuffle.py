my_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    mid_deck = len(my_deck) // 2
    left_part = my_deck[:mid_deck]
    right_part = my_deck[mid_deck:]
    my_new_deck = []
    for new_deck in range(mid_deck):
        my_new_deck.append(left_part[new_deck])
        my_new_deck.append(right_part[new_deck])
    my_deck = my_new_deck
print(my_deck)