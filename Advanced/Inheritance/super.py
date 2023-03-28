class Person:
    country = "Pak"
    
    
    def __init__(self):
        print("Initializing Person")
    
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()                # calling constructor of Parent class i-e Person class
        print("Initializing Employee")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()             #takeBreath() of parent class i-e person class is called
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"


    def __init__(self):
        super().__init__()                  # calling constructor of Parent class i-e Employee class
        print("Initializing Programmer")
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()       # this will call the takeBreath() of base class (since the Programmer class is inheriting Employee class , so by using super.takeBreath()  , takeBreath() of base class which is Employee class , is called )
        print("I am a Progarmmer so I am breathing++..")




p = Person()
p.takeBreath()                       

e = Employee()
e.takeBreath()                       

pr = Programmer()
pr.takeBreath()                      
                    
