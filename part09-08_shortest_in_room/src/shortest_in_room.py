# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons_in_room = []
        self.combined_height = 0

    def add(self, person):
        self.persons_in_room.append(person)
        self.combined_height += person.height

    def is_empty(self):
        return (len(self.persons_in_room) == 0)
    
    def print_contents(self):
        print (f'There are {len(self.persons_in_room)} persons in the room, and their combined height is {self.combined_height} cm')
        for persons in self.persons_in_room:
            print (f"{persons.name} ({persons.height} cm)")
    
    def shortest(self):
        if len(self.persons_in_room) == 0:
            return None
        else:
            shortest = self.persons_in_room[0]
            for person in self.persons_in_room:
                if person.height < shortest.height:
                    shortest = person
        return shortest
    
    def remove_shortest(self):
        shortest = self.shortest()
        if shortest is None:
            return None
        else:
            self.persons_in_room.remove(shortest)
            self.combined_height -= shortest.height
        return shortest




if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()