member_in_group = int(input())
number_of_nights = int(input())
transport_cards = int(input())
bilets_for_museum = int(input())

nights = 20
card_for_transport = 1.6
bilet = 6

total_sum_for_nights = number_of_nights * nights
total_sum_for_transport = transport_cards * card_for_transport
total_sum_for_bilets = bilet * bilets_for_museum
total_sum_for_member = total_sum_for_nights + total_sum_for_transport + total_sum_for_bilets
total_sum = total_sum_for_member * member_in_group * 1.25


print(f"{total_sum:.2f}")
