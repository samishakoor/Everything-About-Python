class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 40

    @property                          # totalSalary(self) has now become getter function
    def totalSalary(self):
        print(self)
        return self.salary + self.salarybonus

    @totalSalary.setter                # totalSalary(self,val) has now become setter function
    def totalSalary(self, val):
        self.salarybonus = val - self.salary      #here salarybonus is an instance variable 

e = Employee()
print(e.totalSalary)          #e.totalSalary will call totalSalary()  only the syntax of calling totalSalary function is changed from e.totalSalary() to e.totalSalary because of @property   
e.totalSalary = 5800          # calling totalSalary(self,val) function because of @totalSalary.setter
print(e.salary)               # here the e.salary will display that salary(class variable i-e,5600) because no instance variable(salary) is created/initialized at that time
print(e.salarybonus)          #now salarybonus is no more a class variable because an instance variable (salarybonus) is initialized in totalSalary(self,val) function and the output is 200
print(Employee.salarybonus)               # 40 because class variable cannot be changed by the object of that particular class
