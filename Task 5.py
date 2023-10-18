#TASK-5 CONTACK BOOK
#Internship Task

contacts = []

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    if not contacts:
        print("No contacts to display.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}")

def search_contact():
    query = input("Enter a name or phone number to search: ")
    found = False
    for contact in contacts:
        if query in (contact.name, contact.phone):
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            found = True
    if not found:
        print("Sorry Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if name == contact.name:
            contact.phone = input("Enter the new phone number: ")
            contact.email = input("Enter the new email address: ")
            contact.address = input("Enter the new address: ")
            print("Contact updated successfully.")
            return
    print("Sorry Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if name == contact.name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Sorry Contact not found.")

while True:
    print("Contact Management System:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exit")
        break
    else:
        print("Invalid choice.")
