# Write a program that translates messages from Morse code to English (capital letters).
#   Use this page to help you (without the numbers). The letters will be separated by a space (' ').
#       Each word is separated by a ' | '.
# Print the found words on one line, separated by a space.

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..'}

morse_text = input().split()
decrypted_word = ""

for code in morse_text:
    if code == "|":
        decrypted_word += " "
        continue
    for key, value in morse_dict.items():
        if code == value:
            decrypted_word += key
            break
print(decrypted_word)
