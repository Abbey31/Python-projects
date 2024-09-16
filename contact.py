contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email addreess: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {"phone":phone,"email":email}
        print(f"Contact {name} added.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contact_book:
        print(f"Name:{name},phone:{contact_book[name]['phone']},email:{contact_book[name]['email']}")
    else:
        print("Contact not found.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact_book[name] = {"phone":phone, "email":email}
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def view_all_contacts():
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name:{name}, phone:{details['phone']},email:{details['email']}")
    else:
        print("Contact book is empty")

while True:
    print("\n---- Contact Book Menu ----")
    print("1.Add a new contact")
    print("2.Search for a contact")
    print("3.Edit a contact")
    print("4.Delete a contact")
    print("5.View all contacts")
    print("6.Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_all_contacts()
    elif choice == "6":
        print("Exiting  contact Bye!👋👋👋")
        break
    else:
        print("Invalid choice try again!")
