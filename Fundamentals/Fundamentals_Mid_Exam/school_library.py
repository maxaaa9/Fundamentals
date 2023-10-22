

my_books = input().split("&")

while True:
    command = input().split(" | ")
    if command[0] == "Done":
        break
    elif command[0] == "Add Book":
        book_name = command[1]
        if book_name in my_books:
            continue
        else:
            my_books.insert(0, book_name)
    elif command[0] == "Take Book":
        name_of_book = command[1]
        if name_of_book in my_books:
            my_books.remove(name_of_book)
        continue
    elif command[0] == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        if first_book in my_books and second_book in my_books:
            one = my_books.index(first_book)
            two = my_books.index(second_book)
            my_books[one], my_books[two] = my_books[two], my_books[one]
    elif command[0] == "Insert Book":
        book_for_insert = command[1]
        if book_for_insert not in my_books:
            my_books.append(book_for_insert)
    elif command[0] == "Check Book":
        if int(command[1]) < len(my_books):
            index_of_book = my_books[int(command[1])]
            print(index_of_book)

print(f"{', '.join(my_books)}")
