# Contact book dictionary
contact_book = {}

def add_contact(name, phone):
    contact_book[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    if contact_book:
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts to display.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
