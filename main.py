from arrays import lists
from CreateTuples import createTuples
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("My age is " + str(self.age))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #p1 = Person("John", 36)
    #p1.myfunc()
    #lists()
    createTuples()






