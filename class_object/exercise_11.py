class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        if not book.strip():
            return 'Please enter a valid book.'
        else:
            self.books.append(book)
    def remove_book(self,book):
        if book not in self.books:
            return 'Book not found!'
        else:
            self.books.remove(book)
    def check_book(self,book):
            if book in self.books:
                return f"'{book}'are in the library."
            else:
                return f"'{book}' are not in the library."
    def total_books(self):
        return f"Total book  in the library is: {len(self.books)}"
        

library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

print(library.total_books())

library.remove_book("Java")
print(library.total_books())

print(library.check_book("Python"))
print(library.check_book("Java"))
print(library.remove_book("Ruby"))
