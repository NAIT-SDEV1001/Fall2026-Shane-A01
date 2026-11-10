from .book import Book

class Library:
    def __init__(self,name: str)->None:
        self.name = name
        self.books = []

    def __str__(self)-> str:
        return self.name

    #method to add books to the library
    def add_book(self,book: Book)->None:
        self.books.append(book)

    #list all the books
    def list_books(self)->None:
        print("Books in library:")
        if not self.books:
            print("No books in library")
        else:
            for book in self.books:
                print(book)
    #method to search for a book by title
    #if found, return the book object
    #otherwise return None
    def find_book(self, title: str)->Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None




# library1 = Library("Good Books")
# library1.add_book(Book("hello world","that guy",100,50))
# library1.list_books()





