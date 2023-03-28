'''


#Class variable or member variable allocates the memory of that variable 
#for every single object of the same class. It may or may not have default value

#Instance variable is specific to individual object of that class.
#Every single object must initialise that instance variable in some way, 
#or optionally having default value.


class Person:
    country = "Pak"
    name="Sami"
    salary=100                      #class variable 
    
    
    def update_salary(self,sal):
        self.salary=sal                # here the salary is an instance variable not class variable , class variable can't be changed or updated in methods or member functions unless it is changed by the class itself
        
        
p=Person()
print(p.salary)                         # since the salary(as an instance variable) is not created , therefore p.salary will access the salary(class variable) )
print(Person.salary)                    # 100
p.update_salary(500)                    # here, the salary(i-e, self.salary) in update_salary(500) is instance variable not class variable (no matter they have same name) 
print(Person.salary)                    # 100 because salary is class variable and cant be changed unless it is changed by class
print(p.salary)                         # here the salary accesses by p object is an instance variable not a class variable (if salary(instance variable) is not created/initialized then p.salary will display the salary (class variable i-e,100) )

'''

#in order to use/access (to change or update) 
# class variables inside the member functions ,
# we will use the following syntax:


class Person:
    country = "Pak"
    name="Sami"
    salary=100                      #class variable 
    
    #Method 1 (old method) to change/update the class variable
    def update_salary1(self,sal):
        self.__class__.salary=sal         
        
    #Method 2 to change/update the class variable
    @classmethod
    def update_salary2(cls,sal):         #cls has a reference of class and can be used to change/update class variables
        cls.salary=sal     
        
        
p=Person()
print(p.salary)                         #  p.salary will access the salary(class variable) )
print(Person.salary)                    # 100
p.update_salary2(500)                   # here, the salary in update_salary1(500) is class variable  and is updated as well using class method 
print(Person.salary)                    # 500 because salary is class variable and is changed/updated by using class method 
print(p.salary)                         # 500 because class variable has now been changed 
        
        
        