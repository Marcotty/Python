class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#String representation
    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)
    
p1 = Person("John", 36)
print(p1)