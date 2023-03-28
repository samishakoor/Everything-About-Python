                 # taking input and displaying output in python
name=input('What is your name : ');
print('Name : ' +name);

favcolor=input('Enter your favourite color : ');
print(name + ' favourite color is '+ favcolor );

# By default , "name" and "favcolor" variable is storing input as a string

# birthyear=input("Enter Birth Year : ");
# age=2019-birthyear;                #this will give an error because birth year is a string by default and we are subtracting a string from an integer value 
# print(age);

# this problem can be solved by:

birthyear=input("Enter Birth Year : ");
age=2019-int(birthyear);                # converting string from birthyear into integer 
print(age);
print();

# or this problem can also be solved by taking input and storing it into its respective data type
birthyear=int(input("Enter Birth Year: "));               #takes input and store it in as an integer
age=2019-birthyear;
print(age);
print();
