
                                #Example #1 (simple inheritance)

class Employee:
    company="google"
    
    def show_details(self):
        print("Show details")
        
        
class Programmer(Employee):
    company="youtube"
    
    def show_name(self):
        print("show name")
        
        
e=Employee();
p=Programmer();                

p.show_details();                 # calling the method of parent class with the object of child class (if child class has the same overriden function show_details() then p.show_details() will not call parent class show_details() function , instead it will call the child class show details() function as illustrated in example 2) 
e.show_details();




                                #Example #2

class Employee1:
    company="google"
    
    def show_details(self):
        print("Show details of employee")
        
        
class Programmer1(Employee1):
    company="youtube"
    
    def show_details(self):
        print("show details of programmer")
        
        
e1=Employee1();
p1=Programmer1();                 

p1.show_details();            # now the show_details of child class is called by the object p1 of child class       



                 