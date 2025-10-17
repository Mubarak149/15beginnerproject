contact = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    if not contact:
        print("No contacts available.")
        return
    else:
        print("Contact List:")
        for name, phone in contact.items():
            print(f"Name: {name}, Phone: {phone}")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        print(f"Contact found: Name: {name}, Phone: {contact[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact:
        del contact[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")