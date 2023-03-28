try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:        #when the code in try block is successfully running (not throwing error) then after the running of code in try block, system directly goes to else block to implement the code written in else block
    print("We were successful")
    
    
#the else block will run if exception is not thrown (try block successfully run)   
# but if the code in try block throws an error then except block will run (else block will not run)
 