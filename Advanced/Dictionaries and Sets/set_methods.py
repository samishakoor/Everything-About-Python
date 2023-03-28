# Creating an empty 
b = set()         
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))      # we can add tuple in a set but we cannot add a list in a set
print(b)


## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

## Length of the Set
print(len(b)) # Prints the length of this set

m={20,20.0,'20'}       # '20' is a string
print(len(m))          #prints 2 because 20 and 20.0 is counted as one



## Removal of an Item
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())          #removes a random/arbitrary item/element from a set and returns that item as well
print(b)


#union (returns a new set which is the union of both sets)
c=b.union({(2,4,5),4,9})      # a set containg tuple and some values is unioned with set b and returns the whole new set to c 
print(c) 

#intersection
c=b.intersection({(2,4,5),4,9})      # returns an empty set because given set and set b has no elements as common elements
print(c) 

#clear
c.clear()              # makes the whole set empty 
print(c)

fav={}              # an empty dictionary
print(type(fav))    # class 'dict'

