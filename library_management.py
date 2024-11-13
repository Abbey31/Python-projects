class Library:
    def __init__(self,members,books):
        self.books = []
        self.members = []

class Book(Library):
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def borrow_book(self):
        for book in self.books:
            print(f"{book} borrowed")

    def add_book(self,book):
        for book in self.books:
            self.books.append(book)
            print(f"new {book} added")
    def remove_book(self):
        for book in self.books:
            del[book]
            print(f"{book} deleted")

    def list_books(self):
        return[self.books for book in self.books]

class Members(Library):
    def __init__(self,name,age):
        self.name = name
        self.age = age   

    def add_new_member(self,name,age):
        self.name = name
        self.age = age
        
    
        member = input("Name: "),input("Age:")
        self.members.append(member)
        return f"{member}"
        

    def remove_member(self):
        
        member = input("name: "),input("Age: ")

        del([member])
        print(f"member{member} deleted")

# new = Members()
# new.add_new_member("Sheu",11)
iwe = Book("money","eru")
iwe.list_books()
#print(new.add_new_member())

    
            