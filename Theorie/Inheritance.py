class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  #The child's __init__() function overrides the inheritance of the parent's __init__() function.
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.year = year
        # Super() function available
        super().__init__(fname, lname)
        self.year = year
        self.graduationyear = 2019
        
x = Student("Mike", "Olsen", 2019)
x.printname()