'''
Classes are made up of attributes/properties(member variables) and
methods(member function).

There are two types of attributes 
1. Class Attributes  (related to the class only and present inside the class and can't be changed by object , it is changed only by the class but can be accessed sing object of that class)
2. Instance Attributes (related to object of a particular class , declared or initialized outside the class)

'''


#Example1 (importance of class and instance attributes)

class RailwayForm:
    formtype="Railwayform"                    # form type is class attribute and is can only be changed by class not the object of that class but object can access that variable

    #methods
    def display_passengers(self):
              print(f"Name is {self.name}")
              print(f"Train is {self.train}")

    def display_formtype(self):
        print(self.formtype)


#now we have come out of class and now we will intantiate object of that class

rail=RailwayForm()            # rail is the object of class Railwayform
rail.name="Sami"              # declaring initializing an instance variable at the same time (but we can seperately declare it and initialize it when we want)
rail.train="Express"          # declaring and initializing an instance variable
rail.display_passengers();    # calling a method with object of that particular class

print(rail.formtype)          # the object of class is accesssing the class variable but it can't change or modify it

rail.display_formtype();
RailwayForm.formtype="EngineForm";         #now we have changed the class attribute by using class because only class can change class variable not object of that class (object can only access class variable)
rail.display_formtype();

rail.display_formtype();           # now the formtype class variable is changed/modified by using class name but still object of that class can always access it


#Example2  (what will happen if the name of both (class and instance) variables are same?)
# so the answer is : instance attribute take preference overclass attributes duringassignment and retrieval

class RailwayEmployee:
    salary="100";

    def print_salary(self):
        pass                            #pass means that there is noting in this method


employee1=RailwayEmployee()
employee2=RailwayEmployee()

print(employee1.salary);           #since instance variable is not created with employee1 object so it will use salary variable as a class variable and displays 100

employee2.salary=50;               #now the employee2 object has an instance variable named salary (similar to class variable)
print(employee2.salary);           # since the instance variable is created with employee2 oject and initialized so this time so employee2 object will use salary variable as an instance variable and displays 50

#Example3  (importance of 'self')
#self in python is same as this in c++
#self is automatically created when an object is created

class Employee:
    company="TinTash"

    def print_salary1(self,greet):         # self is related to that oject which calls that print_salary method
        print(f"The salary is {self.salary}\n{greet}")      # jo object ye method call kre ga uss ke sath jo salary(instance variable) attatch(initialize) ho gi wohi salary yaha print hogi

    def print_salary2(slf,greet):          # we can change the name of self to any name but this will not affect the role of self, whatever name we set instead of self, it will always play the role of self (like in this line we use slf instead of self , we can also change self to sami,harry etc wahtever name we want but role will be same)
         print(f"The salary is {slf.salary}\n{greet}") 
        


sami=Employee();
sami.salary=120000;
sami.print_salary1("Thanks!");           #now sami.salary is related to that self (it means that , that salary will be printed wchic is associated with sami object)

sami.print_salary2("Congrats!")




# Example4 (static method) 
#  static method is used when we dont want to use self in our class methods (sometimes we need a function that does not us self parameter)

class Greet:

    @staticmethod            # now we can avoid using self in methods because we declare our method as static method (to declare a method as astatic method we'll write @staticmethod on one line before the prototype of that method)
    def show_greet(name):
        print(f"Welcome {name}");


obj=Greet();
obj.show_greet("Sami")



#Example5 (constructor)
# constructor will provide the advantage that instead of declaring and initializing instance variables(ofcourse outside the class) , we can declare and initialize those variables(not instancevariable but play the role same as instance variable plays the role) in constructor

class NewEmployee:
    company = "Google"

    def __init__(self, name, salary, subunit):       #actually in constructor , we are initializing the instance variables (for example , name,salary and subunit are instance variables here)
        self.name = name                        
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")


obj1=NewEmployee("Sami",120000,"IT");        #these parameters will automatically initialized when we create an object (these arguments are used to initialize the instance variables in constructor)
obj1.getDetails();

print()
print()


#Example6 (Encapsulation)             

'''
when we use private identifier (in python , private identifier is denoted by double underscore 
for example __age (age is private) , also remember that only class variables(not instance variables) 
can be declared as private ) ,so the object of class(who has private variable) could not access 
that variable beacause we declared it private and in this way , we can achieve encapsulation (encapsuation is
only achieved by declaring class variables (or may be class methods) as private)
# __age variable could not be accessed outside the class
'''

class Student:
    __name ="Ali"                #declaring class variable "name" as private variable (noe this variable cannot be accessed by the object of that class) , now the name variable will always be used as __name


    def __init__(self):
       print(self.__name)
       print("Constructor called")
       self.__display_name()         #calling private method in a constructor
    def __display_name(self):        #now the display_name() ,ethod is also declared as private method(cannot accessed outside the class)                    
        print(self.__name + " Welcome To Python World")

    def get_name(self):
        return self.__name

s=Student()                # __name can only be accessed outside the class through constructor or some sort of getter etc
#print(s.__name)           #displays an error because __name cannot be accessed outside the class because name is a private variable
#s.__display_name()        #displays an error because __display_name vannot be accessed outside the class because it is a private method
print(s.get_name())        # __name is accessed(not directly accessed with object) because of getter method  



