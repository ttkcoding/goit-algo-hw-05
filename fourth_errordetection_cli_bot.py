#create function for except all mistakes and give information what's wrong
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter contact Name please."
        except KeyError:
            return "Contact not found"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_user_phonenumber(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def user_phonenuber(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    return contacts[name]
    

def all_users_and_numbers(contacts):
    return '\n'.join(f'Name: {name}  Phone: {phone}' for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_user_phonenumber(args, contacts))
        elif command == "phone":
            print(user_phonenuber(args, contacts))
        elif command == "all":
            print(all_users_and_numbers(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()