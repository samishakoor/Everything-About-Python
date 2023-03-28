# Filter Syntax: list(filter(function_name, list_name))
def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

# a lambda function
g10 = lambda num: num>10

l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
print(list(filter(greater_than_5, l)))   # the function "greater_than_5(num)" will take each element of list as num (argument passed in 'greater_than_5' function)  and applies the condition present in greater_than_5 function , if the element satisfies the specific condition then that element will be filtered out and returned to a new list ("list" in our case) 

print()

print(list(filter(g10, l)))     # here the function passed to filter function is a lambda function which is possible




#another example of filter function


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 54, 23, 55, 90, 60]

a = filter(lambda a: a%5==0, l)         # here a%5 is the condition on which each element in list 'l' is filtered out (if the element of list 'l' satisfies the condition then this element is filtered out and returned to a new list named 'list' in our case )
print(list(a))





'''
1. filter function is a bit similar to map function because it
also takes the two arguments (function and list) but filter function
filters the elements of list on the basis of some certain conditions
(those conditions are given in that function which has to apply on every
element of list)

2. if a specific element of list(list given as an argument to filter function) 
satisfies the condition given in the function(function given as an argument to filter function) 
then that element(who satisfid the condition in function) will be filtered
and returned to a new list

3. filter function returns the filtered elements in another new list

4. filter function can be applied on tuples as well


5. the filter function can accept lambda function as an argument

'''