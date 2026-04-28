class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Wohhhh!..")
class Cat(Animal):
    def speak(self):
        print("Meaowwww")

#creating objects on the above classes

# dog = Dog()
# cat = Cat()
# animal = Animal()

#looping over all classes directly with creating objects

for pet in [Dog(),Cat(),Animal()]:
    pet.speak()

#Polymorphism
class Sum:
    def add(self, a,b=0,c=0):
        return a+b+c

add = Sum()
print(add.add(5))
print(add.add(5,10))
print(add.add(5,10,15))