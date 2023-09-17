word = input()

lowercase_word = word.lower()

counter = 0
counter += lowercase_word.count("sand")
counter += lowercase_word.count("water")
counter += lowercase_word.count("fish")
counter += lowercase_word.count("sun")

print(counter)