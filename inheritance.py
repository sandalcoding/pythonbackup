#n = input("Name: ")
#print("My name is", n + ".")


class student:
  age = 12

  def __init__(self, name):
    self.name = name

  def namePrint(self):
    print("Hi, my name is", self.name + ".")


student1 = student("Jonathan")
student2 = student("Justin")

student1.namePrint()
student2.namePrint()

print(student1.age)