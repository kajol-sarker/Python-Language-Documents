# Python Project - Contact Book App

contact = {}  # Dictionary to store contacts

def ShowFunction():
    print("\nName \t\t Phone")
    print("---------------------------")
    for key in contact:
        print(f"{key} \t\t {contact.get(key)}")

while True:
    choice = input("\n1. Add New Contact \n"
                   "2. Search Contact \n"
                   "3. Display Contact \n"
                   "4. Edit Contact \n"
                   "5. Delete Contact \n"
                   "6. Exit \n"
                   "Enter your choice (1–6): ")

    if choice == "1":
        Name = input("Enter the name: ")
        Phone = input("Enter phone number: ")
        # Optionally: Email = input("Enter email: ") — not used here
        contact[Name] = Phone
        print(f"✅ Contact '{Name}' added successfuly.")

    elif choice == "2":
        Search_Contact = input("Enter name to search: ")
        if Search_Contact in contact:
            print(f"📞 {Search_Contact}'s contact is: {contact[Search_Contact]}")
        else:
            print("❌ Contact not found.")

    elif choice == "3":
        if not contact:
            print("📭 Contact book is empty.")
        else:
            ShowFunction()

    elif choice == "4":
        Edit_Contact = input("Enter contact name to edit: ")
        if Edit_Contact in contact:
            Phone = input("Enter new phone number: ")
            contact[Edit_Contact] = Phone
            print("✅ Contact updated successfully.")
            ShowFunction()
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        Del_Con = input("Enter contact name to delete: ")
        if Del_Con in contact:
            DelConfirm = input("Are you sure you want to delete? (y/n): ").lower()
            if DelConfirm in ["yes", "y"]:
                contact.pop(Del_Con)
                print("🗑️ Contact deleted successfully.")
                ShowFunction()
            else:
                print("❎ Deletion cancelled.")
        else:
            print("❌ Contact not found.")

    elif choice == "6":
        print("👋 Exiting Contact Book. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 6.")



