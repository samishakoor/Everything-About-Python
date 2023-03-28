     #built-in modules(just like libaraies) in python

                           #random module
import random;


print(random.randint(10,20));    #prints any random number from 10 to 20  (10 and 20 are included)
print(random.randrange(10,20))   # returns a random number from 10 to 19 (10 is included but 20 is not) 
print(random.uniform(3,9))       # prints a float random number between 3 and 9

for i in range(3):                  # for loop will run 3 times
    print(random.random());         #prints a float random number between 0 and 1
print();

for i in range(3):
    print(random.randint(10,20));         #prints any random number from 10 to 20  (10 and 20 are included)
print();

members=['sami','haseeb','ali','waqar'];
mem=random.choice(members);               # select any random member from  list 'members'
print(mem);
print();


random.shuffle(members)                 # shuffle(change the order/index of items) the items of list 'members
print(members)


#example of rolling a dice
def dice_roll():
    first=random.randint(1,6);
    second=random.randint(1,6);
    return first,second;

print(dice_roll());



                              #DateTime Module

import datetime


x=datetime.datetime.now()          # prints current date and time
print(x)


#creating datetime object

y=datetime.datetime(2022,2,22)
print(y)
print()

#other datetime modules


a=x.strftime("%y")      # year nnumber(short version)
print(a);
print();
b=x.strftime("%Y")      # year number(full version)
print(b);
print();
c=x.strftime("%B")       # month name(full version)
print(c);
print();
d=x.strftime("%b")        # month name(short version)
print(d);
print();
e=x.strftime("%M")        #minute
print(e);
print();
f=x.strftime("%m")         #month number
print(f);
print();
g=x.strftime("%H")        # hours in 0-24 format
print(g);
print();
h=x.strftime("%I")        #hours in 0-12 format
print(h);
print();
i=x.strftime("%p")    #AM/PM
print(i);
print();

