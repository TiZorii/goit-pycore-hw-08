from record import Record
from address_book import AddressBook
from pickle_operations import load_data, save_data
from datetime import datetime, timedelta

def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone = args[0], args[1]
            print(add_contact(name, phone, book))

        elif command == "change":
            name, old_phone, new_phone = args[0], args[1], args[2]
            print(change_phone(name, old_phone, new_phone, book))

        elif command == "phone":
            name = args[0]
            print(show_phones(name, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            name, birthday = args[0], args[1]
            print(add_birthday(name, birthday, book))

        elif command == "show-birthday":
            name = args[0]
            print(show_birthday(name, book))

        elif command == "birthdays":
            print(show_birthdays(book))

        else:
            print("Invalid command.")

def add_contact(name, phone, book):
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    record.add_phone(phone)
    return message

def change_phone(name, old_phone, new_phone, book):
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number changed."
    else:
        return "Contact not found."

def show_phones(name, book):
    record = book.find(name)
    if record:
        return f"Phones for {name}: {', '.join(str(p) for p in record.phones)}"
    else:
        return "Contact not found."

def show_all(book):
    contacts = [str(record) for record in book.data.values()]
    if contacts:
        return "\n".join(contacts)
    else:
        return "Address book is empty."

def add_birthday(name, birthday, book):
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

def show_birthday(name, book):
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    elif record:
        return "No birthday set for this contact."
    else:
        return "Contact not found."

def show_birthdays(book):
    upcoming_birthdays = []
    for record in book.data.values():
        if record.birthday:
            today = datetime.today()
            next_week = today + timedelta(days=7)
            if record.birthday.value.month == next_week.month and record.birthday.value.day <= next_week.day:
                upcoming_birthdays.append((record.name.value, record.birthday.value.strftime('%d.%m')))
    if upcoming_birthdays:
        return "\n".join([f"{name}'s birthday on {date}" for name, date in upcoming_birthdays])
    else:
        return "No upcoming birthdays."

if __name__ == "__main__":
    main()
