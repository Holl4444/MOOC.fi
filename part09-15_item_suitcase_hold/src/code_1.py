# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        if self.__check_name(name):
            self.__name = name
        else:
            return ValueError('Name cannot be an empty string.')
        if self.__check_weight(weight):
            self.__weight = weight
        else:
            return ValueError('Weight cannot be negative.')

    def __check_name(self, name: str):
        return name != ''

    def __check_weight(self, weight):
        return weight >= 0

    def name(self):
        return self.__name
        
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'
       

class Suitcase:
    def __init__(self, carry_capacity: int):
        self.carry_capacity = carry_capacity
        self.__contents = []

    @property
    def carry_capacity(self):
        return self.__carry_capacity
    
    @carry_capacity.setter
    def carry_capacity(self, carry_capacity: int) -> None:
        if carry_capacity >= 0:
            self.__carry_capacity = carry_capacity
        else:
            raise ValueError('Carry capacity must be positive.')
        
    def add_item(self, item: Item) -> None:
        remaining_capacity = self.carry_capacity - sum([item.weight() for item in self.__contents])
        if remaining_capacity >= item.weight():
            self.__contents.append(item)

    def print_items(self) -> None:
        for item in self.__contents:
            print(item)

    def weight(self) -> int:
        remaining_capacity = self.carry_capacity - sum([item.weight() for item in self.__contents])
        return self.carry_capacity - remaining_capacity
    
    def heaviest_item(self) -> Item | None:
        current_heaviest = self.__contents[0]
        weight = self.__contents[0].weight()
        if len(self.__contents) > 0:
            for item in self.__contents[1:]:
                if item.weight() > weight:
                    current_heaviest = item
                    weight = item.weight()
            return current_heaviest
        else:
            return None
                    

    def __str__(self) -> str:
        remaining_capacity = self.carry_capacity - sum([item.weight() for item in self.__contents])
        return f'{len(self.__contents)} {'item' if len(self.__contents) == 1 else 'items'} ({abs(self.carry_capacity - remaining_capacity)} kg)'

class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__current_load = 0
        self.__contents = []
    
    @property
    def max_weight(self):
        return self.__max_weight
    
    @max_weight.setter
    def max_weight(self, max_weight: int):
        if max_weight >= 0:
            self.__max_weight = max_weight
        else:
            raise ValueError('Maximum weight cannot be negative.')
        
    def add_suitcase(self, suitcase: Suitcase):
        if self.max_weight - self.__current_load - suitcase.weight() >= 0:
            self.__contents.append(suitcase)
            self.__current_load += suitcase.weight()

    def print_items(self):
        for suitcase in self.__contents:
            suitcase.print_items()

    def __str__(self):
        return f'{len(self.__contents)} {'suitcase' if len(self.__contents) == 1 else 'suitcases'}, space for {self.max_weight - self.__current_load} kg'


if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()