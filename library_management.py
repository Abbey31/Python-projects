class Library:
    def __init__(self,books,members):
        self.books = books
        self.members = members



class Book:
    def __init__(self,title,author,isbn,is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = False

    def borrow(Book):
        books = {}
        for title,author in books.items():
            print(f"{title}:{author}")

    def read_book():
        pass 

class Members:
    def __init__(self,membership_id,check_out):
        self.membership_id = membership_id
        self.check_out = check_out

    def add_new_member():
        user_id = {}
        name = input("Name: ")
        
        if name in user_id:
            print("user already exixts")
        else:
            age = input("Age: ")
            user_id[name] = age
            print("new member:{name} with age :{age} added successfully")

    def remove_member():
        user_id = []
        name = input("name: ")
        if name not in user_id:
            print("Not Found")
        else:
            age = input("age: ")
            del(user_id[name,age])

    def check_in():
        pass
            