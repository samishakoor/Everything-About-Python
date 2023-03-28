 # strings in python (strings always start from 0 index)
                     
#  course[2,9] means print the course string from 2nd index to 8th index (but remember the first character of string is always present at Oth index)                    

# single line string
course="Python's course for beginners";
print(course);
course='Python course for "beginners"';
print(course);
#multi-line string
description= ''' 
Hello Sami!
I am a computer Scientist
I am Learning Python from Mosh
I am really enjoying this tutorial,
Regards!
'''
print(description);

course="Hello WorLd";
#string indexing
print(course[0]);                     # H
print(course[1]);                     # e
print(course[2]);                     # l
print(course[-1]);                    # d    (reading string from reverse because of mainus sign)
print(course[-2]);                    # L    (reading string from reverse because of minus sign)
print();
#string slicing
print(course[1:-1]);       # ello WorL
print(course[1:4]);        # print all the characters(string) between index 1 and index 4 i-e , ell
print(course[1:]);         # print string(characters) after index 1 onwards i-e, ello WorLd
print(course[:4]);         # print string(characters) before index 4 i-e, Hell
print();
#string slicing with increments/decrements   (remember when there is increment of 1 (SKIP NO CHARACTER) and when there is increment of 2(skip one character) and so on)
print(course[0::1])        #prints string from start of string(start from 0th index) with increment of 1 (increment of 1 means to somply iterate one character after another without skipping any character) and runs until the string ends(prints Hello World)
print(course[0::2])        #prints string from start of string with increment of 2(skips one character after printing each character)and runs until the string ends (prints Hlo Wrd)

print(course[1:9:2])       #prints the string from 1st index to 8thth index while skipping one character (increment of 2) after printing one character   

print(course[-1::-1])      #prints the whole string in reverse direction until the string ends (prints dLroW olleH)
print(course[-1::-2])      #prints the whole string in reverse direction with decrement of 2 (skipping one character after printing one character in reverse direction) and runs until the string ends (prints drWolH) 

print(course[-1:5:-1])     #prints the last 4 characters(but in reverse direction) , [-1:5:-1] indicates that , -1 means to start from last index of string, 5 means to iterate the string upto 4th index , -1 means to skip no charater while iterating string(decrement of 1)           




                           #formatted strings
first='sami';
last='shakoor';

course=first + '[' + last + ']'+ ' is a coder';  #this is not a formatted string
print(course);
course=f'{first} [{last}] is a coder';          # this is a formatted string
print(course);
print();

                            # string methods
course="Hello I am a Programmer";


#len() method
print(len(course));            # prints length of string
print();
#upper()  method
print(course.upper());         #converts string to uppercase
print();
#lower()  method
print(course.lower());         #converts string to lowercase
print();
#capitalize()  method 
print(course.capitalize());    # only capitaizes the first character of string and the rest of the string is in small letters (prints Hello i am a programmer)
print();
#title()  method
print(course.title());         # capitalize first letter of each word in a string (prints Hello I Am A Programmer)
print();
# simply prints the string
print(course);                 # original string is printed without any change
print();
#split() method
a=course.split();              # split() method splits the whole string by space (jaha jaha string ma space hoti ha waha waha se string split ho jaati ha) and then store the splitted string in a list (we can also call it the "conversion of string to a list")
print(type(a));                # here the 'a' is a list because split() function splits the whole string by spaces and store those split strings in a list 
print(a);
print();
# find()  method
print(course.find('I'));       #returns index of given character otherwise eturns -1 (case-sensitive)
print(course.find('Programmer')); #returns index of P beacause Programming starts with P
print(course.find('e',2))         #returns the index of 'e' in course string but iteration of string starts from 2nd index (i-e, the first two characters(at 0th and 1st index) are not considered during reading string)but -1 is printed/returned if desired character is not found in string (prints the 'e' present in 'Programmer') 
print();
#replace()  method
print(course.replace('Programmer','Computer Scientist'));         # replaces string with given string
print();
# in 
print('Hello' in course);     #returns true if hello is present in course string otherwise returns false
print();

#index()   method
print(course.index('e'));       # returns the index of 'e' in the string if 'e' is present in the string but if the string is not present then, it will genrate an error
print(course.index('Programmer'))  # similar to course.find('Programmer') method but it will generate an error if Programmer is not present in string
#print(course.index('z'));      # dsiplay an error because 'z' is not present in course string
print(course.index('e',2));     #prints index of e in course string but iteration starts from 2nd index (0th anf Ist indexes will be ignored didn't matter if e is present in 0th or 1st index or not)
#print(course.index('z',2));    # displays an error beacuse 'z' is not present when iteration is started from 2nd index

print()

'''
The functions of find and index methods are same but the only difference is the
find returns -1 is character or string is not present in string while on the
other hand, index displays an error if desired character/string is not present in string

'''


#format()   method

#1.named indexes
txt1="Two even numbers are {a} and {b}".format(a=20,b=40)               
print(txt1)       # simply prints txt1


txt7="Welcome to {fname} {lname}".format(fname="Python",lname="programming")
print(txt7)

txt4="Two even numbers are {a:>10} and {b:>10}".format(a=20,b=40)
print(txt4)       # a:>10 means the value of a is printed on the space of 10 characters (but written on left side)

txt5="Two even numbers are {a:<10} and {b:<10}".format(a=20,b=40)
print(txt5)        # a:<10 means the value of a is printed on the space of 10 characters (but written on right side)


txt6="Two even numbers are {a:^10} and {b:^10}".format(a=20,b=40)
print(txt6)     # a:^10 means the value of a is printed on the space of 10 characters (but written in center)

print();

#2.numbered indexes
txt2="Welcome to {0:^10} {1}".format("Python", 12345)
print(txt2)          # 0:^10 means that Python is written(in centre) on the space of 10 characters (for example , python has 6 characters but it has to be written on 10 characters , so 10-6=4 , it means 2 spaces are present on left side of python and 2 spaces are present on right side of pthon which means python containing 6 characters is present in centre with four spaces and in that way total 10 spaces are covered )
print();

#3.empty placeholders 
txt3="Welcome to {} {}".format("Python","programming")
print(txt3)

print()


#isalpha()  method
word1="abxdfnienvaicnn"
print(word1.isalpha())           # prints true if string contains only alphabets(digits and spaces are not allowed)  otherwise returns false       (prints true in this case)
word2="askaj asmmsoimd"
print(word2.isalpha())             #returns false because space is present between two words
print();
#isdigit()   method
dig1="12345"
print(dig1.isdigit())      #returns true if string contains only numbers(digits) otherwise it returns false
dig2="123sami"
print(dig2.isdigit())      # returns false beacuse string contains some alphabets too
print();
#isalnum()  method
print(dig2.isalnum())      # returns true if the string is alphanumeric (alphabets and letters are mixed but it must not contain special characters and spaces as well)

string1="ssad12@3"
print(string1.isalnum())        # returns false because special character is present which is not allowed

print()


#chr()     method       (used for converting ascii number into its corressponding specific character)
y=chr(65)                
print(y)                   #prints 'A' beause 65 is ascii of A
print(type(y))             # y is a string
print()

#ord()    method       (used for converting an alphabet into its corressponding specific number)
z=ord('A')                
print(z)                   #prints 65 beause ascii of A is 65
print(type(z))             # z in an integer
print();
