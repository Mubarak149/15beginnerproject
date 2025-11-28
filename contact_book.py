contactsbook = {
    "Alice": "09123445348",
    "Bob": "09234556789",
}

def add_contact(name, phone_number):
    contactsbook[name] = phone_number
    print(f"Contact {name} added.")


def view_contacts():
    for name, phone_number in contactsbook.items():
        print(f"{name}: {phone_number}")

def search_contact(name):
    if name in contactsbook:
        print(f"{name}: {contactsbook[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contactsbook:
        del contactsbook[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")