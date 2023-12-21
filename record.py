from contact_data import *

   
class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        if Phone.is_valid_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise ValueError("Error: the phone number must be 10 digits")

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if Phone.is_valid_phone(new_phone):
            for item in self.phones:
                if item.value == old_phone:
                    item.value = new_phone
                    return
            raise ValueError(
                f"Error: the phone number {old_phone} not found in the record."
            )
        else:
            raise ValueError("Error: the phone number must be 10 digits")

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item.value
        raise ValueError(f"Error: the phone number {phone} not found in the record.")

    def add_birthday(self, date):
        self.birthday = Birthday(date)
