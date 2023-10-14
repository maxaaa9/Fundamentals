def vowels_remover(string):
    text_without_vowels = [x for x in string if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
    return "".join(text_without_vowels)


text = input()
print(vowels_remover(text))
