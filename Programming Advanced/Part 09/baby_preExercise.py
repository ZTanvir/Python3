
# WRITE YOUR SOLUTION HERE:
# Note! Do not change the class Person!

from tkinter.font import names


class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        return -1

#


class Product:
    def __init__(self, name: str, unit: int):
        self.name = name
        self.unit = unit


shopping_cart = []
milk = Product("Milk", "litre")
egg = Product("Egg", 12)
shopping_cart.append(milk)
shopping_cart.append(milk)
shopping_cart.append(egg)
for item in shopping_cart:
    print(item.name, item.unit)

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name


dog_gang = []
dog1 = Dog("Rex")
dog_gang.append(dog1)
dog_gang.append(dog1)
dog_gang.append(Dog("Rex"))
dog_gang.append(Dog("Rqw"))

for dog in dog_gang:
    print(dog)
print("update index-0:")
dog_gang[0].name = "xeR"
for dog in dog_gang:
    print(dog)
print("change index 1:")
dog_gang[2].name = "Tux"
for dog in dog_gang:
    print(dog)

# dictonary 
class Student:
    def __init__(self,name,credit):
        self.name = name
        self.credit = credit

student_info = {}
student_info["1"] = Student("roton",4)
student_info["2"] = Student("Tata",2)
for key in student_info:
    print(student_info[key].credit)

# Self use
class Vocabulary:
    def __init__(self):
        self.words = []

    def check_word(self,word):
        if not word in self.words:
            self.words.append(word)
    
    def print_words(self):
        for word in sorted(self.words):
            print(word)
    
    def longest_word(self):
        longest_word_is = ""
        longest_word_size = 0
        for word in self.words:
            if len(word) > longest_word_size:
                longest_word_size = len(word)
                longest_word_is = word
        return longest_word_is

word_list = Vocabulary()
word_list.check_word("python")
word_list.check_word("java")
word_list.check_word("c")
word_list.check_word("python")
word_list.print_words()
print(word_list.longest_word())
# object as argument to a function
class House:
    def __init__(self,name:str,place:str):
        self.name = name
        self.place = place

    def __str__(self) -> str:
        return f"name:{self.name},place:{self.place}" 

def change_Name(house:House):
    house.name = "Dhaka"

bondhon = House("Bondhon","Ecb dhaka")
print(bondhon)
change_Name(bondhon)
print(bondhon)