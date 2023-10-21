def decipher(words) -> str:
    message = []
    for word in words:
        digits = ""
        new_word = []
        for element in word:
            if element.isdigit():
                digits += element
            else:
                new_word.append(element)
        new_word[0], new_word[-1] = new_word[-1], new_word[0]
        message.append((chr(int(digits)) + "".join(new_word)))
    message = " ".join(message)
    return message


secret_message = input().split()
print(decipher(secret_message))
