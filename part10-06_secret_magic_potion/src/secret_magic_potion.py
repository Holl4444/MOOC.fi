# Write your solution here:
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients: list[tuple[str, float]] = []

    # Password added to both methods to satisfy linter
    def add_ingredient(self, ingredient: str, amount: float, password: str):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self, password: str):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name: str, password: str):
        self.password = password
        self.name = name
        super().__init__(self.name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if name == "":
            raise ValueError("name cannot be blank.")
        self._name = name

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        if password == "":
            raise ValueError("Password must not be an empty string.")
        self._password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if ingredient == "":
            raise ValueError("The ingredient cannot be nothing.")
        if amount < 0:
            raise ValueError("The amount cannot be negative")
        if not password == self._password:
            raise ValueError("Invalid password.")
        super().add_ingredient(ingredient, amount, password)

    def print_recipe(self, password: str):
        if password != self._password:
            raise ValueError("Invalid password.")
        super().print_recipe(password)


if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")

    diminuendo.print_recipe("pocushocus")
