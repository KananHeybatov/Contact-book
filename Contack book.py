import json
contacts = {}
try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}
while True:
    print("\n1. View contacts"
          "\n2. Add contact"
          "\n3. Search contacts"
          "\n4. Delete contact"
          "\n5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            if not contacts:
                print("No contacts found")
            else:
                for name, info in contacts.items():
                    print(f"{name} — Phone: {info['phone']}, Email: {info['email']}")

        elif choice == 2:

            name = input("Enter name: ").strip().title()
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts[name] = {"phone": phone, "email": email}
            print(f"Contact {name} added!")

            with open("contacts.json", "w") as f:
                json.dump(contacts, f)

        elif choice == 3:

              search = input("Enter search contact: ").strip().title()
              if search in contacts:
                  info = contacts[search]
                  print(f"{search} — Phone: {info['phone']}, Email: {info['email']}")
              else:
                  print("Contact not found!")

        elif choice == 4:

            name = input("Enter name: ").strip().title()
            if name in contacts:
                del contacts[name]
                print(f"Contact {name} deleted!")
                with open("contacts.json", "w") as f:
                    json.dump(contacts, f)
            else:
                print("Contact not found!")

        elif choice == 5:
            break

    except ValueError:
        print("Please enter a number")