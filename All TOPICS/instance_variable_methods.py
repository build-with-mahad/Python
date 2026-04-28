class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade 
    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Grade : {self.grade}")
    def is_eligible(self):
        if self.age >= 18:
            print(f"{self.name} is eligible for admission")
        else: 
            print(f"{self.name} is not eligible for admission")
student1 = Student("Ali", 16,7)
student2 = Student("Sara", 18,10)
print(student1.name)
print(student1.age)
print("*************")
print(student2.name)
print(student2.age)
print("*************")
student1.info()
student1.is_eligible()
print("*************")

student2.info()
student2.is_eligible()
