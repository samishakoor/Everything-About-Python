 # Membership Operators ("in" and "not in") 
# Membership operators returns true or false                     

str="hello";
print('h' in str)

if('H' not in str):
    print("H is not present in str")




                      #Identity Operator ("is" and "is not") 
# Identity operators returns true or false    
# similar to comparison operators ("==" and "!=")

a=15
b=12
c=15

if a is c:
    print("Yes")
else:
    print("No")


if a is not b:
    print("Yes")
else:
    print("No")



                     #Bitwise Operators 
# AND -> &
# 0R  -> |
# Xor -> ^

x=6
y=2

print(x&y)                         #in decimal form
print(bin(x&y))                    #in binary form 

print(x|y)                         #in decimal form
print(bin(x|y))                    #in binary form 

print(x^y)                         #in decimal form
print(bin(x^y))                    #in binary form 

 
                      # Logical Operators

# and operator
hasHighIncome=True;
hasGoodCredit=True;

if hasHighIncome and hasGoodCredit:
    print("eligible for loan");
else:
    print("not eligible for loan")

print();

x=6;
y=2;

if x==6 and y==2:
    print("x=6 and y=2");
else:
    print("x is not 6 and y is not 2");

print();


# or operator
hasHighIncome=False;
hasGoodCredit=True;

if hasHighIncome or hasGoodCredit:
    print("eligible for loan");
else:
    print("not eligible for loan")

print();

x=6;
y=2;

if x==6 or y==5:
    print("x=6 and y=2");
else:
    print("x is not 6 and y is not 2");

print();


# not operator (changes true to false or false to true)
hasHighIncome=True;
hasGoodCredit=False;

if hasHighIncome and not hasGoodCredit:
    print("eligible for loan");
else:
    print("not eligible for loan")

print();

if hasHighIncome or not hasGoodCredit:
    print("eligible for loan");
else:
    print("not eligible for loan")

print();

#comparison operators (==,!=,>,<,<=,>=)

x=6;
y=5;

if x!=6 :
    print("x is not 6");
elif y==2:
    print("y is 2");
else:
    print("x is 6 and y is 5");

print();

if x>=5:
    print("x is greater than 5");
elif y<=10:
    print("y is less than 10");
elif x<2:
    print("x is less than 2");
elif y>10:
    print("y is greater than 10");
else:
    print("Noooooo");

print();
