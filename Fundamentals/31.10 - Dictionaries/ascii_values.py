# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value.
# Try solving that problem using comprehension.

list_of_characters = input().split(", ")
character_dictionary = {x: int(ord(x)) for x in list_of_characters}
print(character_dictionary)
