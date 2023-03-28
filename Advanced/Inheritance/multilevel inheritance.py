class Person:
    country = "Pak"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()                       #takeBreath in Person class is called


e = Employee()
e.takeBreath()                       # since takeBreath() is present in Employee class so the takeBreath() in Employee class is called
print(e.company)

pr = Programmer()
pr.takeBreath()                      # calls takeBreath() function of programmer class (if takeBreath() is not present in programmer class then pr object will access or call the takeBreath() function of the nearest possible parent class which is Employee class in this case )
print(pr.company)                    # prints fiverr
print(pr.country)                    # prints country variable of person class which means that pr object can access the grandparent class variables and functions(if employee class has country variable then pr object will call the country variable of Employee class) , it means that the child class object access the nearest possible variable or function of parent class 
