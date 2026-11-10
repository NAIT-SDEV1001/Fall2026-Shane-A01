from library_tools.book import Book
from library_tools.library import Library

def main():
    library = Library("Gooder books")
    print(library)
    library.add_book(Book('a','b',100,10))
    library.add_book(Book('c','d',200,20))
    library.add_book(Book('e','f',300,30))

    library.list_books()

    #search for a book
    search_result = library.find_book('r')
    if search_result is None:
        print("Book not found")
    else:
        print(f"Found: {search_result}")

if __name__ == "__main__":
    main()