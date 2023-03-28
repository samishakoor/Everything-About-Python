# Example 1 (without Global variable)

a = 54            
def func1(a):
     
    print(f"Print statement 1: {a}")
    a = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {a}")

func1(a)
print(f"Print statement 3: {a}")

# Example 2 (with Global variable)

b = 54   # Global variable
def func1():
    global b 
    print(f"Print statement 1: {b}")
    b = 8 # Local Variable if global keyword is not used
    print(f"Print statement 2: {b}")

func1()
print(f"Print statement 3: {b}")



