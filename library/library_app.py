from library_tools.book import Book
from library_tools.library import Library

def main():
    library = Library("Gooder books")
    print(library)
    library.add_book(Book('a','b',100,10))
    library.add_book(Book('c','d',200,20))
    library.add_book(Book('e','f',300,30))

    #add another book but only if it is not already there(uses __eq__)
    new_book = Book('c','t',200,20)
    if new_book not in library.books:
        library.add_book(new_book)
    else:
        print("Book with that title and author already in the library")


    library.list_books()

    #search for a book
    search_result = library.find_book('r')
    if search_result is None:
        print("Book not found")
    else:
        print(f"Found: {search_result}")



if __name__ == "__main__":
    main()