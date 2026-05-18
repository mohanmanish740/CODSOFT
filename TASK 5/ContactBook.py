contact_storage_list = []

def add_contact_function():
    contact_name_value = input("Enter name: ")
    contact_phone_value = input("Enter phone: ")
    contact_email_value = input("Enter email: ")
    contact_address_value = input("Enter address: ")

    contact_storage_list.append({
        "name": contact_name_value,
        "phone": contact_phone_value,
        "email": contact_email_value,
        "address": contact_address_value
    })

    print("Contact added successfully!")

def view_contacts_function():
    if len(contact_storage_list) == 0:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for contact_item in contact_storage_list:
            print(contact_item["name"], "-", contact_item["phone"])

def search_contact_function():
    search_input_value = input("Enter name or phone to search: ")

    found_flag_value = False

    for contact_item in contact_storage_list:
        if search_input_value in contact_item["name"] or search_input_value in contact_item["phone"]:
            print(contact_item)
            found_flag_value = True

    if not found_flag_value:
        print("Contact not found.")

def update_contact_function():
    update_input_value = input("Enter name to update: ")

    for contact_item in contact_storage_list:
        if contact_item["name"] == update_input_value:
            contact_item["phone"] = input("Enter new phone: ")
            contact_item["email"] = input("Enter new email: ")
            contact_item["address"] = input("Enter new address: ")
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact_function():
    delete_input_value = input("Enter name to delete: ")

    for contact_item in contact_storage_list:
        if contact_item["name"] == delete_input_value:
            contact_storage_list.remove(contact_item)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    menu_choice_value = input("Enter your choice: ")

    if menu_choice_value == "1":
        add_contact_function()

    elif menu_choice_value == "2":
        view_contacts_function()

    elif menu_choice_value == "3":
        search_contact_function()

    elif menu_choice_value == "4":
        update_contact_function()

    elif menu_choice_value == "5":
        delete_contact_function()

    elif menu_choice_value == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
