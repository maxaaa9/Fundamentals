# Write a program, which keeps a dictionary with synonyms. The key of the dictionary will be the word.
#   The value will be a list of all the synonyms of that word. You will be given a number n – the count of the words.
#   After each term, you will be given a synonym, so the count of lines you should read from the console is 2 * n.
#   You will be receiving a word and a synonym each on a separate line like this:
# ⦁	{word}
# ⦁	{synonym}
# If you get the same word twice, just add the new synonym to the list.
# Print the words in the following format:
# {word} - {synonym1, synonym2 … synonymN}

synonym_dictionary = {}
count_of_words = int(input())

for words in range(count_of_words):
    word = input()
    synonym_of_word = input()
    if word not in synonym_dictionary:
        synonym_dictionary[word] = []
    synonym_dictionary[word].append(synonym_of_word)

for key, values in synonym_dictionary.items():
    print(f"{key} - {', '.join(values)}")
