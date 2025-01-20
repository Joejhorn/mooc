# Write your solution here:
class Item:
    __slots__ = ['__name', '__weight']
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    def name(self):
        return self.__name
    def weight(self):
        return self.__weight
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
class Suitcase:
    def __init__(self, weight):
        self.max_weight = weight
        self.items_in_suitcase = []
        self.total_weight = 0

    
    def add_item(self, item):
        if self.max_weight > item.weight():
            self.items_in_suitcase.append(item)
            self.max_weight -= item.weight()
            self.total_weight += item.weight()

    def __str__(self):
        if len(self.items_in_suitcase) != 1:
            item_desc = "items"
        else:
            item_desc = "item"
        return f'{len(self.items_in_suitcase)} {item_desc} ({self.total_weight} kg)'
    
    def print_items(self):
        for item in self.items_in_suitcase:
            print(item)
    
    def weight(self):
        total_weight = 0
        for item in self.items_in_suitcase:
            total_weight += item.weight()
        return total_weight
    
    def heaviest_item(self):
        heavy_object = self.items_in_suitcase[0]
        for item in self.items_in_suitcase:
            if item.weight() > heavy_object.weight():
                heavy_object = item
        return heavy_object
                
class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cargo_in_plane = []
        self.space_left = max_weight

    def add_suitcase(self, suitcase):
        if self.space_left > suitcase.weight():
            self.cargo_in_plane.append(suitcase)
            self.space_left -= suitcase.weight()

    def __str__(self):
        if len(self.cargo_in_plane) == 1:
            suitcases = 'suitcase'
        else:
            suitcases = 'suitcases'

        return f'{len(self.cargo_in_plane)} {suitcases}, space for {self.space_left} kg'
    
    def print_items(self):
        for suitcases in self.cargo_in_plane:
            suitcases.print_items()


           

    


       


if __name__ == '__main__':


    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # adas_suitcase = Suitcase(10)
    # adas_suitcase.add_item(book)
    # adas_suitcase.add_item(phone)

    # peters_suitcase = Suitcase(10)
    # peters_suitcase.add_item(brick)

    # cargo_hold = CargoHold(1000)
    # cargo_hold.add_suitcase(adas_suitcase)
    # cargo_hold.add_suitcase(peters_suitcase)

    # print("The suitcases in the cargo hold contain the following items:")
    # cargo_hold.print_items()

    hold = CargoHold(100)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    hold.print_items()

