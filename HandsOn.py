class Person:
  def __init__(self, name, pre, mid, fin):
    self.__name = name
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin
  def Grade(self):
    print("The term grade is: ", round((self.__pre + self.__mid + self.__fin)/3, 2))
  def display(self):
    print(self.__name)
    print(" Prelim grade is: ", self.__pre)
    print(" Midterm grade is: ", self.__mid)
    print(" Finals grade is: ", self.__fin)

class Student1(Person):
  pass
class Student2(Person):
   pass
class Student3(Person):
  pass

std1 = Student1("Student 1", 98, 95, 97)
std1.display()
std1.Grade()
std2 = Student2("Student 2", 91, 90, 92)
std2.display()
std2.Grade()
std3 = Student3("Student 3", 88, 86, 90)
std3.display()
std3.Grade()
