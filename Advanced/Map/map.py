def square(num):
    return num*num


l = [1, 2, 4]


# Method 1
print(list(map(square, l)))           # square function is applied on every element of list 'l'  , we can see clearly that square function takes one argument num (i-e, square(num))  which means each element of list 'l' is considered as num while applying square function to each element of list 'l' (and this is what map function do) and finally all the resulted elements(on which square functions is applied) is returned to a new ist named "list" 


# Method 2 (old method (alternative method) to do the same)
l2 = []
for item in l:
    l2.append(square(item))
print(l2)




'''
The syntax of map function is:

                map(function_name,list_name)

1. So, the map function takes two arguments function name and list name

2. map function ,actually, applies the given function (which is passed 
as an argument to map function )on the EVERY single element/item of that list 
which is passed as an argument to map function  and  returns the every single Element 
(in which the function is being applied) to a new list 

3. Therefore we can say that map function maps every element of given list onto
another list after applying the given function on every element of that given list 

4. filter function returns the filtered elements in another new list

5. map function can also be applied on tuples

'''