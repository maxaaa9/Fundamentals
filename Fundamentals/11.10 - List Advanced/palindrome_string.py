def palindrome_checker(word: str) -> list:
    my_palindrome_list = [x for x in word.split() if x[::-1] == x]
    return my_palindrome_list


words = input()
my_palindrome = input()

result = palindrome_checker(words)
palindrome_counter = result.count(my_palindrome)
print(f"{result}\nFound palindrome {palindrome_counter} times")
