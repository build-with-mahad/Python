class Car:
    def __init__(self,color):
        self.color =  color
    def drive(self):
        print(f"{self.color} car is moving!..")

car = Car("White")
car.drive()

class Bike:
    name = "Unique"
    def drive(self):
        print(f"{self.name} is moving!...")

bike = Bike()
bike.drive()

class Car1:
    color = "Blue"
    def drive(self):
        print(f"{self.color} honda is moving!..")
    def setColor(self,color):
        self.color = color
car1 = Car1()
car1.drive()
car1.setColor("Green")
car1.drive()

class Dog:
    def __init__(self):
        self.name = "Buddy"
    def bark(self):
        print(f"{self.name} was Barking")

dog = Dog()
dog.bark()

class Cat:
       def __init__(self,color,breed):
         self.color= color
         self.breed =  breed 
       def CatDetails(self):
          print(f"The cat color is {self.color} and the breed is {self.breed}")
cat = Cat("White","Persian")
cat.CatDetails()
cat.color = "Black"
cat2 = Cat("Gray","Furry")
cat2.CatDetails()
print(cat.color)
