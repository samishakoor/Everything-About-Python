try:
    a = int(input("Enter a number: "))
    c = 1/a                         # this code will throw an error if invalid input is entered by user
    print(c)
    
except ValueError as e:             #  this except block will run if code in line no 3 throws value error (when some variable of other datatype (i-e, string) is input by user instead of integer (beacuse data type of a is integer in this case))
    print("Please Enter a valid value") 

except ZeroDivisionError as e:      # this except block will run when we divide some number by 0
    print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")



# there are two except blocks here, which block will run depends on type of error being thrown

# we can use more than one except blocks with one try block (but which block runs depend on the error thrown by code in try block)

 
                              # another example


try:
    a = int(input("Enter a number: "))
    c = 1/a                         # this code will throw an error if invalid input is entered by user
    print(c)
    
except ValueError as e:             #  this except block will run if code in line no 3 throws value error (when some variable of other datatype (i-e, string) is input by user instead of integer (beacuse data type of a is integer in this case))
    print("Please Enter a valid value") 

except ZeroDivisionError as e:      # this except block will run when we divide some number by 0
    print("Make sure you are not dividing by 0") 
except:                             # this except block will run when some error (other than ValueError and ZeroDivisionError) is thrown 
    print("some unknown/other is thrown")         



print("Thanks for using this code!")

