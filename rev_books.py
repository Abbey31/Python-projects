class Library: 
    def __init__(self,books,members):
        self.books = []
        self.members = []
        def add_books(self,book):
             if book in self.books:
                print("book already in the library")
             else:
                 self.books.append(book)
                 print(f"new book {book} added")
class Book(Library):
     def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
     def list_books(self): 
        for book in self.books:
             return book
class Members(Library):
     def __init__(self,member): 
        self.member = member
     def add_new_member(self):
         register = input("Name: "), input("Age: ") 
         if register in self.members:
            print(f"{register} already registered")
         else: 
            self.members.append(register)
     def list_members(self,member):
         for member in self.member:
            return member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        if book in self.books:
            print("Book already in the library")
        else:
            self.books.append(book)
            print(f"New book '{book.title}' added")

    def list_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Pages: {book.num_pages}")

    def add_member(self, member):
        if member in self.members:
            print(f"{member.name} is already a member")
        else:
            self.members.append(member)
            print(f"New member '{member.name}' added")

    def list_members(self):
        if not self.members:
            print("No members in the library")
        else:
            for member in self.members:
                print(f"Name: {member.name}, Age: {member.age}")

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Example usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
library.add_book(book1)
library.add_book(book2)

# Listing books
library.list_books()

# Adding members
# member1 = Member("Alice", 30)
# member2 = Member("Bob", 25)
# library.add_member(member1)
# library.add_member(member2)

# Listing members
#library.list_members()
#Key Changes:
#Separation of Concerns: Book and Member classes are now separate from the Library class.

#Initialization: Removed unnecessary parameters from Library's __init__ method.

#Methods: Added methods to list books and members within the Library class.

#Example Usage: Provided an example of how to use the classes.

#This should give you a clearer structure and better understanding of OOP in Python. Feel free to ask if you have any questions or need further assistance!