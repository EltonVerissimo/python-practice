from book import Book

book1 = Book("Uma breve história do tempo", "Stephen Hawking", 1996)
book2 = Book("the call of cthulhu", "HP. Lovecraft", 1926)

book1.lend()
print(book1)

print(book1.checkIfIsAvaliable(1996))

print(book2)