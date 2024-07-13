class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        if name in self.contacts:
            print("Contact already exists!")
        else:
            self.contacts[name] = number
            print("Contact added successfully!")

    def update_contact(self, name, number):
        if name in self.contacts:
            self.contacts[name] = number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Number: {self.contacts[name]}")
        else:
            print("Contact not found!")

    def view_contacts(self):
        for name, number in self.contacts.items():
            print(f"Name: {name}, Number: {number}")

contact_book = ContactBook()

while True:
    print("1. Add contacts")
    print("2. Update contacts")
    print("3. Delete contacts")
    print("4. Search contacts")
    print("5. View all contacts")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contact_book.add_contact(name, number)
    elif choice == "2":
        name = input("Enter name: ")
        number = input("Enter new number: ")
        contact_book.update_contact(name, number)
    elif choice == "3":
        name = input("Enter name: ")
        contact_book.delete_contact(name)
    elif choice == "4":
        name = input("Enter name to search: ")
        contact_book.search_contact(name)
    elif choice == "5":
        contact_book.view_contacts()
    elif choice == "6":
        break
    else:
        print("Invalid option!")
