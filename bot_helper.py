"""
This module provides a simple command-line assistant bot to manage a contacts list.
The bot supports the following commands:
- add <name> <phone>: Adds a new contact with the given name and phone number.
- phone <name>: Retrieves the phone number for the given contact name.
- change <name> <new_phone>: Changes the phone number for the given contact name.
- all: Displays all contacts in the contacts list.
- hello: Greets the user.
- close/exit: Exits the assistant bot.
"""

def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Parameters:
    user_input (str): The input string from the user.

    Returns:
    tuple: A tuple containing the command and a list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Parameters:
    args (list): A list of arguments containing the name and phone number.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    if len(args) != 2:
        return "Error: Add command requires exactly 2 arguments (name and phone)."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def get_number(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Parameters:
    args (list): A list of arguments containing the name and phone number.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    if len(args) != 2:
        return "Error: Add command requires exactly 2 arguments (name and phone)."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Change the phone number for an existing contact.

    Parameters:
    args (list): A list of arguments containing the name and new phone number.
    contacts (dict): The contacts dictionary.

    Returns:
    str: A message indicating the result of the operation.
    """
    if len(args) != 2:
        return "Error: Change command requires exactly 2 arguments (name and new phone)."
    name, new_phone = args
    old_phone = contacts.get(name)
    if old_phone is not None:
        contacts[name] = new_phone
        return "Contact updated"
    else:
        return "Name not found"

def show_all(contacts):
    """
    Show all contacts in the contacts dictionary.

    Parameters:
    contacts (dict): The contacts dictionary.

    Returns:
    str: A formatted string of all contacts.
    """
    if not contacts:
        return "No contacts found."
    result = "\n" + "-" * 30 + "\n"
    result += f"{'Name':<15} {'Phone Number':<15}\n"
    result += "\n" + "-" * 30 + "\n"
    for name, phone in contacts.items():
        result += f"{name:<15} {phone:<15}\n"
        result += "\n"
    return result

def main():
    """
    Main function to run the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_number(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
