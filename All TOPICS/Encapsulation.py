class Student:
    def __init__ (self,grade):
        self.__grade= grade

std = Student(10)
# print(std.__grade) #Error 

class Student1:
    def __init__(self,grade):
        self.__grade = grade
    def get__grade(self):
        return self.__grade
std1 = Student1(12)
print(std1.get__grade())

class Student:
    def __init__(self,name,grade):
        self.__grade = grade 
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0<=grade and grade <=100:
            self.__grade = grade
        else:
            print("Invalid Grade")

std = Student("Ali",80)
std.set_grade(23)
print(std.get_grade())
