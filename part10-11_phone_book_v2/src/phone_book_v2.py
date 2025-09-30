# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.check_name(name)
        self.__numbers: list[str] = []
        self.__address: str = ""

    def name(self):
        return self.__name

    def check_name(self, name: str):
        if not name:
            raise ValueError("Name cannot be an empty string.")
        self.__name = name

    def address(self):
        if not self.__address:
            return None
        return self.__address

    def numbers(self) -> list[str]:
        return self.__numbers

    def add_number(self, number: str):
        if not len(number) > 3:
            raise ValueError("That doesn't look like a telephone number.")
        self.__numbers.append(number)

    def add_address(self, address: str):
        if not address:
            raise ValueError("That doesn't look like an address.")
        self.__address = address

    def __str__(self):
        return f"{self.name()}:\n{self.numbers()}\n{self.address()}"


class PhoneBook:
    def __init__(self):
        self.__persons: dict[str, Person] = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            newPerson = Person(name)
            self.__persons[name] = newPerson
        Person.add_number(self.__persons[name], number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            newPerson = Person(name)
            self.__persons[name] = newPerson
        Person.add_address(self.__persons[name], address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if not person:
            print("address unknown\nnumber unknown")
            return
        if not person.numbers():
            print("number unknown")
        else:
            for number in person.numbers():
                print(number)
        if not person.address():
            print("address unknown")
        else:
            print(person.address())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()


if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    phonebook.add_number("Eric", "1337")
    phonebook.add_address("Eric", "Rabbithole Fields")
    phonebook.add_address("Sahar", "Gravelly Drive")
    phonebook.add_number("Jennifer", "1066")
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Sahar"))
    print(phonebook.get_entry("Jennifer"))
