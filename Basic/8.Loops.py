       #loops
#while loop

i=1;
while i<=5:
    print('*'*i);
    i+=1;
print("DONE!");
print();

#number guessing game as an example of while loop
secret_number=9;
guess_count=0;
guess_limit=3;

while guess_count<guess_limit:
    guess=int(input("Guess: "));
    guess_count+=1;
    if guess==secret_number:
        print("You Won!");
        break;
else:
    print("Sorry, You Failed!");
print();

#for loop

for item in "Python":               #store each character of string "Python" in item variable and print it one by one using for loop
    print(item);
print();

for item in ["SAMI","Haseeb","Ali","Iqbal"]:
    print(item);
print();

for item in [1,2,4,9]:
    print(item);
print();

items=[1,2,4,9];
for item in items:
    print(item);
print();

for item in range(10):          #print all integers from 0 to 9  (in increment mode)    (for loop will start its execution from 0 and runs until 9)
    print(item);
print();

for item in range(5,10):          #print all integers from 5 to 9 in increment mode (10 is not included) i-e, 5,6,7,8,9   (for loop will start its exexution from  5 and runs until 9 )  
    print(item);
print();

# if range contains three arguments then the third argument indicates the increment/decrement mode  (if positive then increment, if negative then decrement)
for item in range(5,10,2):          #print all integers from 5 to 9 with difference of 2(skipping one number after printing one number) i-e, 5,7,9
    print(item);
print();

for item in range(10,0,-1):          #print all integers from 10 to 1 (backword counting)   , the last argument of range is -1 and this indicates that the for loop will iterate in reverse direction (while skipping no characters) but for loop will start from 10 and runs unti1 1 is reached 
    print(item);
print();

# normally in case when range has three arguments and first argument is larger than the secong argument, then it means the for loop will iterate in reverse direction and third argument determines the level of increment/decrement


#important example 1 to understand range
str="sami shakoor"
for a in range(1,8,2):               # range(1,8,2) means "from 1st index to 7th index while skipping one character"
    print(str[a])                    # print a,i,s,a on seperate seperate line

print()
print()

#important example 2 to understand range
for b in range(11,-1,-1):           # range(11,-1,-1) it means 11 is the length of str(for loop starts from 11th index) , -1 means for loop will iterate till 0th index  , -1 means the decrement of 1(no skipping of characters while reading characters in string) , so it means, iterate the string in reverse direction while skipping no character(decrement of -1)
    print(str[b])                   # prints imas shakoor (but one character on one line)

print()
print()


prices=[10,20,30];
total=0;
for price in prices:
    total+=price;
print(f"Total : {total}");        # Total : 60 


# Nested Loops (nested for loop)

for x in range(4):
    for y in range(3):
        print(f'({x},{y})');
print();

#specific pattern pritning using nested loops

numbers=[5,2,5,2,2];
for x_count in numbers:
    output='';                 #initializing output variable with null
    for count in range(x_count):
        output=output+'x';
    print(output);
print();
