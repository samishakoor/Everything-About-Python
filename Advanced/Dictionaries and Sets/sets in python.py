# sets looks similar to dictionary because of curley brackets

'''
There are some properties of sets:
1.unordered
2.unindexed (cannot be accessed by index)
3.don't contain duplicate values
4.no way to change/update the items in set
'''


s={1,3,4,6,7,2,1}
a={}         # remember: a is empty dictionary not an empty set

print(type(s))         # prints type of s which is class 'set'
print(type(a))         # prints type of a which is class 'dictionary'

print(s)               # set dont displays repetitive elements (here 1 comes 2 times but displayed 1 time)


# syntax to create an empty set
b=set()          # now b is an empty set
print(type(a))   # prints type of b which is class 'set'
