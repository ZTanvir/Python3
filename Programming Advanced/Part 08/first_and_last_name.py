# Create class Person
class Person:
    # Create attribute name
    def __init__(self, name: str):
        self.name = name

    def devide_full_name(self):
        full_name = self.name
        # Slice the variable in place of space
        divide_full_name = full_name.split(" ")
        return divide_full_name

    # Create method return_first_name
    def return_first_name(self):
        # return the 1st index
        first_name = self.devide_full_name()[0]
        return first_name

    # Create method return_last_name
    def return_last_name(self):
        last_index = len(self.devide_full_name())-1
        last_name = self.devide_full_name()[last_index]
        return last_name


# Test the program
if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())
