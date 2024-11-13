from ref_books import *

library = Library()

# Adding books
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
library.add_book(book1)
library.add_book(book2)

# Listing books
library.list_books()

# Adding members
member1 = Member("Alice", 30)
member2 = Member("Bob", 25)
print(member1.age)