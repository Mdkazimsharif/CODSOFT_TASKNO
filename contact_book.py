contacts = {}

def add_contact():
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    contacts[name] = phone
    print(f"Contact '{name}' added!")


def view_contact():
    if contacts == {}:
        print("Empty contact list!!")
    else:
        print("\n------Contact list---------")
        for key, value in contacts.items():
            print("Name:", key, "\nPhone number:", value)

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!")
    else:
        print(f"Contact {name} does not exist!!")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        phone = int(input("Enter your phone number: "))
        contacts[name] = phone
        print(f"Contact '{name}' updated!")
    else :
        print(f"Contact {name} does not exist!!")

while True:
    print("\nWelcome to the contact book!!")
    print("What would you like to do?")
    print("1. Add contact")
    print("2. View contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        update_contact()
    else:
        break