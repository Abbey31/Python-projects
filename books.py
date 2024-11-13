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