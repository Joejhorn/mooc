# Write your solution here:

class Person:
    def __init__(self, name):
        self.name_split = name.split(' ')
       

    def return_first_name(self):
        return self.name_split[0]


    def return_last_name(self):
        return self.name_split[1]




if __name__ == '__main__':
    if __name__ == "__main__":
        peter = Person("Peter Pythons")
        print(peter.return_first_name())
        print(peter.return_last_name())

        paula = Person("Paula Pythonnen")
        print(paula.return_first_name())
        print(paula.return_last_name())












