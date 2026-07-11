still=True
contactsList = {}

#Class to hold the contact information
class Contact:
    def __init__(self, username, name, phone, email):
        self.username = username
        self.name = name
        self.phone = phone
        self.email = email

#Load all the contacts from the file into the contactsList dictionary
#Using a try-except block to handle the case where the file does not exist
try:
     with open("contact_list.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                username, name, phone, email = line.split(",")
                contactsList[username] = Contact(username, name, phone, email)
except FileNotFoundError:
    print("No saved contacts found. Starting fresh.")


#Add contact function to add a new contact to the contactsList dictionary
def add_contact():
    print(f"Add Contact".center(60, "="))
    print("\n")
    
    user_Username = input("Enter contact username: ")
    
    #check if the username already exists in the contactsList dictionary
    while user_Username in contactsList:
        print(f"Contact with username {user_Username} already exists! \n")
        user_Username = input("Enter a different username: ")
    user_Name = input("Enter contact name: ")
    user_Phone = input("Enter contact phone number: ")
    user_Email = input("Enter contact email: ")
    contactsList[user_Username] = Contact(user_Username, user_Name, user_Phone, user_Email)
    
    save_contacts()
    print("\n")
    print("-" * 60)
    print(f"Contact {user_Username} added successfully!")
    print("-" * 60)
    print("\n")

#View contacts function to display all the contacts in the contactsList dictionary
def view_contacts():
    print(f"View Contacts".center(60, "="))
    print("\n")
    if not contactsList:
        print("No contacts found.")
    else:
        for contact in contactsList.values():
            print("-" * 60)
            print(f"Username: {contact.username}")
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print("-" * 60)
            print("\n")

#Search contacts function to search for a contact in the contactsList dictionary           
def search_contacts():
    print(f"Search Contacts".center(60, "="))
    print("\n")
    search_username = input("Enter contact username to search: ")
    
    #check if the username exists in the contactsList dictionary
    if not search_username in contactsList:
        print(f"Contact {search_username} not found.")
    else:
        contact=contactsList[search_username]
        print("\n")
        print("-" * 60)
        print(f"Username: {contact.username}")
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print("-" * 60)
        print("\n")

#Delete contact function to delete a contact from the contactsList dictionary
def delete_contact():
    print(f"Delete Contact".center(60, "="))
    print("\n")
    delete_username = input("Enter contact username to delete: ")
    if not delete_username in contactsList:
        print(f"Contact {delete_username} not found.")
    else:
        del contactsList[delete_username]
        save_contacts()
        print("\n")
        print("-" * 60)
        print(f"Contact {delete_username} deleted successfully!")
        print("-" * 60)
        print("\n")

#save contacts function to save the contactsList dictionary to a file
def save_contacts():
    with open("contact_list.txt", "w") as file:
        for contact in contactsList.values():
            file.write(f"{contact.username},{contact.name},{contact.phone},{contact.email}\n")


while still:
    print(f"Contact Manager".center(60, "="))
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contacts\n4. Delete Contact\n5. Save Contacts\n6. Exit\n")
    print("-" * 60)
    action = input("Enter your choice: ")
    print("-" * 60)
    
    if action == "1":
        add_contact()
        
    if action == "2":
        view_contacts()
        
    if action == "3":
        search_contacts()
    
    if action == "4":
        delete_contact()
    
    if action == "5":
        save_contacts()
        print(f"Save Contacts".center(60, "="))
        print("\n")
        print("-" * 60)
        print("All contacts saved successfully!")
        print("-" * 60)
        print("\n")
    
    if action == "6":
        still = False
        
     
print("Goodbye!")