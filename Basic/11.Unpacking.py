                #unpacking (works with both lists and tuples)       

coordinates=(1,2,3);            # (1,2,3) is a tuple
x,y,z=coordinates;              #instead of doing x=coordinates[0] , y=coordinates[1] , z=coordinates[2]  , we can use a shortcut method for doing this called unpacking
print(x);         #1
print(y);         #2
print(z);         #3
print();