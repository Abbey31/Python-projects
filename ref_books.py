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

