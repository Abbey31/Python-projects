class Library:  
    def __init__(self):  
        self.books = []  
        self.members = {}  

    def add_book(self, book):  
        self.books.append(book)  

    def remove_book(self, isbn):  
        self.books = [book for book in self.books if book.isbn != isbn]  

    def display_books(self):  
        for book in self.books:  
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.is_available}")  

class Book:  
    def __init__(self, title, author, isbn, is_available=True):  
        self.title = title  
        self.author = author  
        self.isbn = isbn  
        self.is_available = is_available  

    def borrow(self):  
        if self.is_available:  
            self.is_available = False  
            return True  
        else:  
            print("Book is not available")  
            return False  

    def return_book(self):  
        self.is_available = True  

class Member:  
    def __init__(self, membership_id):  
        self.membership_id = membership_id  
        self.checked_out_books = []  

    def add_new_member(self, name, age):  
        # Should be added at the library level, using a unique identifier  
        if name not in self.members:  
            self.members[name] = (age, self.checked_out_books)  
            print(f"New member: {name} with age: {age} added successfully")  
        else:  
            print("User already exists")  

    def remove_member(self, name):  
        if name in self.members:  
            del self.members[name]  
            print(f"Member {name} removed successfully")  
        else:  
            print("Member not found")  

# Example usage  
library = Library()  
book1 = Book("1984", "George Orwell", "1234567890")  
library.add_book(book1)  

member1 = Member("M001")  
member1.add_new_member("Alice", 30)  
library.display_books()  