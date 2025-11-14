class Book:
    books = []
    
    def __init__(self, title, author, publishing_year):
        self.title = title
        self.author = author
        self.publishing_year = publishing_year
        self.avaliable = True
        self.books.append(self)
    
    def __str__(self):
        return f"Título: {self.title}, Autor: {self.author}, Ano de publicação: {self.publishing_year}, Disponível: {self.avaliable}"
    
    def lend(self):
        self.avaliable = False
    
    def checkIfIsAvaliable(self, year):
        books_filtered = [str(book) for book in self.books if book.publishing_year == year]
        return books_filtered