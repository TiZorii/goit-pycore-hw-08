from field import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones_str = ', '.join(str(p) for p in self.phones)
        if self.birthday:
            return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {self.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"Contact name: {self.name.value}, phones: {phones_str}"
