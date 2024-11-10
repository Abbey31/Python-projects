from libraries import *
library = Library()  
book1 = Book("1984", "George Orwell", "1234567890")  
library.add_book(book1)  

member1 = Member("M001")  
member1.add_new_member("Alice", 30)  
library.display_books()  