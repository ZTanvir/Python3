
# WRITE YOUR SOLUTION HERE:
# Note! Do not change the class Person!

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

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1

print(l1 is l2)
print(l2 is l3)
print(l3 is l1)