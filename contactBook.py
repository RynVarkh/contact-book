import json
import os

FILE = "contacts.json"

def add():
    name = input("Contact Name: ")
    phnNum = input("Contact Number: ")   # keep as string

    # Load old contacts if file exists
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            contacts = json.load(f)
    else:
        contacts = []

    # Add new contact
    contacts.append({"name": name, "phone": phnNum})

    # Save back to file
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

    print("Contact saved!")

def view():
    if not os.path.exists(FILE):
        print("No contacts yet!")
        return

    with open(FILE, "r") as f:
        contacts = json.load(f)

    if not contacts:
        print("No contacts found!")
    else:
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")

def main():
    print("1. View") 
    print("2. Add")

    choice = input("Choice from above menu: ")   # keep as string

    if choice == "1":
        view()
    elif choice == "2":
        add()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
