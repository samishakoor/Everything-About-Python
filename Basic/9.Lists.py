                               #Lists

#1D LISTS
names=['sami','shaheer','iqbal','asawir','ali'];
print(names);            # output is :  ['sami','shaheer','iqbal','asawir']
print(names[0]);         #output is : sami
print(names[-1]);        #output is : asawir
print(names[3]);         #output is : asawir
print(names[2:]);        #output is: ['iqbal','asawir','ali']
print(names[2:4]);       #output is: ['iqbal','asawir']
print(names[:4]);        #output is : ['sami','shaheer','iqbal','asawir']
print(names);            # original list not affected
print()





            #lists comprehension (another way of creating lists)

'''
List Comprehension is an elegant way to create a list . It is generally more 
compact and faster than normal functions and loops for creating a list
'''


#old method (non-elegant)

lst=[]                         #making an empty list

for i in range(1,101):         # for loop runs from 1 to 100
    lst.append(i)                   
print(lst)
print()


#new method (elegant way)

x=[y for y in range(1,101) ]         #adding numbers in list from 1 to 100
print(x)
print()


z=[a for a in range(1,101) if a%2==0]          #adding even numbers in list from 0 to 100
print(z)
print()

# converting a string into a list using new elegant way

s="Hello"
d=[g for g in s]
print(d)
print()

#finding maximum number in a list
numbers=[2,3,5,6,8,9,10];
max1=numbers[0];
for number in numbers:
    if number>max1:
       max1=number;
print(max1);
print();

#2D LISTS

matrix=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
 ];

print(matrix);         #output is : [ [1,2,3],[4,5,6], [7,8,9] ]
matrix[0][0]=20;
print(matrix);         #output is : [ [20,2,3],[4,5,6], [7,8,9] ]
print();

for row in matrix:
    for item in row:
        print(item);
print();



                                 #List Methods


numbers=[1,4,7,4,6,8,3];


print(numbers[-1])                #prints the last element of list 'numbers'
print()
#max() method
print(max(numbers));              #print the maximum number in the list
print()
# min()
print(min(numbers));              #print the minimum number in the list
print()
# append()
numbers.append(14);                # append method inserts given element at end of list
print(numbers);
print()
# extend()
num=[3,9,5,0]                       # declaring another list
numbers.extend(num)                 #extending the numbers list using num list 
print()
#update()
numbers[5]=20;                     # update the element present at the 5th index in the list
print(numbers);
print()
#insert()
numbers.insert(0,9);               #  inserts 9 at 0th index 
print(numbers);
print()
#remove()
numbers.remove(6);                # removes the given element from list
print(numbers);              
print()
#del()
del(numbers[1])                    # delete the element present at 1st index in numers list 
print(numbers)
print()
#pop()
popped=numbers.pop();              # removes last element from the list and also returns that element which is popped (for print purposes etc)
print(popped);                          
print()
#clear()
#numbers.clear();                # removes everyhing in the list
print(numbers);
print()
#index()
print(numbers.index(4));         # prints the first occurence (index) of given element
print()
#count()
print(numbers.count(4));         # returns the count of how many times '4' occurs in the list
print()
# in
print(9 in numbers);             #returns true if element exists in list otherwise returns false
print()
# not in
print(20 not in numbers);        #returns true because 20 is not present in the list
print()
#sort()
numbers.sort();
print(numbers);                  #prints elements of list in sorted fashion
print()
#reverse()
numbers.reverse();
print(numbers);                  #prints elements of list in reverse fashion
print()
#copy()
numbers2=numbers.copy();         #copies the list into another list
print(numbers2);
print();

#removing duplicates from a list

numbers=[1,2,5,7,2,8,9,7,1];
unique=[];              #creating an empty list

for num in numbers:
    if num not in unique:
        unique.append(num);
print(unique);
print();

