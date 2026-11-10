class Book:
    def __init__(self,title: str, author: str, pages: int, price: float)-> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self)-> str:
        return f"{self.title} by {self.author}"

    #when comparing objects we need to override __eq__ to define what whould be compared
    #for books we will say if the title and author are the same, it is the same book
    def __eq__(self, other: Book) -> bool:
        return self.title == other.title and self.author == other.author

# book1 = Book('a','b',100,10)
# book2 = Book('c','d',200,101)
# book3 = Book('c','d',200,101)

# print(book1)

# print (book3 == book2)#book1.__eq__(book2)