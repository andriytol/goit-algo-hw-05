def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter name and phone number."
        except KeyError:
            return "Please enter an existing name."
        except IndexError:
            return "Please enter a only command"
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
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args, contacts):
    name, *_ = args
    if name in contacts and len(_) == 0:
        return contacts[name]
    raise KeyError


def show_all(args, contacts):
    if len(args) == 0:
        return contacts
    raise IndexError


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case 'close' | 'exit':
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case 'all':
                print(show_all(args, contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
