                   #Functions
#functions having no return type
def greet_user(firstname,lastname):                    # greet_user is name of function and name is parameter
    print(f'Hi , {firstname} {lastname}!');


greet_user("Sami","Shakoor");             # function calling

#functions with a return type

def sum(a,b):
    return a+b

s=sum(3,2);
print(s);                  #5

#another example

def sum(a,b):
   print(a+b);

print(sum(3,5));                #  display None in output screen because there sum function didn't return anything
print();





                                 # zip() function

#we can iterate more then 2 lists/tuples at the same time using zip() function

l1=[1,5,9]
l2=[4,8,3]
l3=[]

for a,b in zip(l1,l2):                 # a stores the elements of list l1 and b stores the elements of list l2  
     print(a,b)                        # print one element from l1 and one element from l2 
     c=a+b                             # takes one element from l1 and one element from l2 and add them and store it in a variable c to store it in a list l3                 
     l3.append(c)

print()
print(l3)     # l3 is the list cntaining the added elements of both lists l1 and l2
print()



# another way to do the same functionality without using zip() function

a=len(l1);           # a is containing the length of list l1

for x in range(a):              # for loop will run a times
    print(l1[x],l2[x])          # print one element from l1 and one element from l2 

