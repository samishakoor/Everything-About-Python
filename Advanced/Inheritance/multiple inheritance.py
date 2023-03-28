                                   #Example #3    (multiple inheritance)
                                   
                                   
                                   
                                   
class Employee2:
    company="google"
    level=10
    
    def show_details(self):
        print("Show details of employee")
        

class Freelancer:
    company="twitter"
    level=0

    def upgrade_level(self):
         self.level+=1
        
class Programmer2(Employee2,Freelancer):     #remember priority matters (Employee2 is inherited first an freelancer is inherited secondly)
    name="sami"
    
    def show_details(self):
        print("show details of programmer")                                   
                                   

p3=Programmer2()
p3.upgrade_level()
print(p3.company)                          # company of Employee2 is printed because Employee2 is inherited first

                  