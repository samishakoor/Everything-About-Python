def greet(name):
    print(f"Good morning, {name}")

print(__name__)          
if __name__ == "__main__":
    n = input("Enter a name\n")
    greet(n)

print("HAHAHAHA")



'''
now the code from line no 6 to line no 7 cannot
be imported in any other file(python module)
'''

'''
in our current case , m07_file2.py is importing
the file m06_file2.py but the code below line no 7
in m06_file2.py cannot be imported to m07_file2.py
because of __name__
'''



'''
the line no 7 means if the code is run in this file
then __name__ is equal to '__main__' and code below line no7
will run but if we import this current file(m06_file1.py) to another 
file/module (m07_file2.py in our case) then due to importing,
the __name__ in this file will become'm07_file2.py' because we run 
the code in m07_file2.py file  and therefore __name__ will not 
equal to __main__ and the code below that condition(line no7) will not
run    
'''



'''
line no 9 will be executed (run) because it does not 
come under __name__==__main__ condition (only thay part of code will not run which 
is under the condition at line no 7)
'''