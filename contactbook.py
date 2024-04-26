class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact
        print("Contact updated successfully.")

    def delete_contact(self, index):
        del self.contacts[index]
        print("Contact deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contacts(query)
            if not results:
                print("No matching contacts found.")
            else:
                print("Search Results:")
                for contact in results:
                    print(f"{contact.name} - {contact.phone_number}")

        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                name = input("Enter new name: ")
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(index, updated_contact)
            else:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
            else:
                print("Invalid index.")

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
