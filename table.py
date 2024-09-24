# contacts = {}

# def add_contacts():
#     number = input("Enter the number you want to add to the contacts list: ")
#     name = input("Enter the name of the contact: ")
#     email = input("Enter the e-mail address: ")
#     if name in contacts:
#         print("Name already exists")
#     else:
#         contacts[name] = {'number':number,'email':email}
# def delete_contacts():
#     name = input("Enter the name of the contact you want to delete: ")
#     if name in contacts:
#         del contacts[name]
#     else:
#         print("Contact does not exist")
# def edit_contacts():
#     name = input("Enter the name of the contact you want to edit: ")
#     if name in contacts:
#         number = input("Enter new number: ")
#         email = input("Enter new email address: ")
#         contacts[name] = {'number':number,'email':email}
#         print(f"Contact {name} updated")
#     else:
#         print("contact does not exist")
# def view_all_contacts():
#     for data,details in contacts.items():
#         print(f"{data} {details}")

# while True:
#     print("1.Add Contacts")
#     print("2.Delete Contacts")
#     print("3.Edit Contacts")
#     print("4.View all contacts")
#     request = input("Enter your choice (1-4): ")
#     if request == "1":
#         add_contacts()
#     elif request == "2":
#         delete_contacts()
#     elif request == "3":
#         edit_contacts()
#     elif request == "4":
#         view_all_contacts()

 