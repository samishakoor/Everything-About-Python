'''
Polymorphism means same function name (but different signatures/arguments) being
used for different types
Polymorphism is achieved by method overloadind/overriding (but remember , method overriding
works with inheritance only)
'''

                #Example1 (method overloading)

class Student:
    
    def display_name(self,name=""):
        print("Hello " + name)


s=Student()
s.display_name()
s.display_name("Sami")
print()
#This is an example of polymorphism because same function display_name() is used with different arguments 


#another example of method overloading in python


class Area:
    def find_area(self,a=None,b=None):              #find_area method can work for 0,1 and 2 arguments
        if a!=None and b!=None:
            print("Area of Rectangle is ",a*b)
        elif a!=None:
            print("Area of Square is ",a*a)
        else:
            print("Nothing to find")


a=Area()
a.find_area(10)
a.find_area(10,20)
a.find_area()
print()





                  #Example2 (method overriding(same function name with same arguments))
#Method overriding is mostly used in inheritance                  
                  
class Father:
    def print_info(self):
        print("I am Father")                  
        
class Child(Father):
    def print_info(self):
        print("I am Child")
        
        
ch=Child()
ch.print_info();    #calls print_info() of 'Child' class because print_info() of child class overrides the print_info() of parent class   
print()        


#but if we want that both child and parent class print_info() functions will be called then:



class Father1:
    def print_info(self):
        print("I am Father")                  
        
class Child1(Father1):
    def print_info(self):
        super().print_info()   #calls the display_info() method of parent class because of super()
        print("I am Child")
        
        
ch1=Child1()
ch1.print_info();
print()



                