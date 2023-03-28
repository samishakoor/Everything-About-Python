from functools import reduce          # this should be written first in order to use reduce function


'''
1. reduce function is also a bit similar to map function as it also receives the two arguments (function,list)

2. reduce function performs sequential computions on a list and returns a single value

3. reduce function returns a single result (single value)

4. the function(passed as an argument to reduce function)  must accept two arguments
beacuse sequential computations are performed on two values at a time

5. reduce function applies the sequential computations on the elements of list(which is passed as an argument
to reduce function) based on that function which is passed as an argument to reduce function

6. sequential computation will depend on the code/condition given in the function (which is passed as an argument
to reduce function) but remember that, the funcntion must receive two arguments

'''


sum = lambda a, b: a+b

l = [1, 2, 3, 4]
val = reduce(sum, l)
print(val)




'''
for example , in this program ,the sequential computation depends on the code given is sum function(lambda function)
which is a+b , now this sequential computation will apply on every two elements of list one by one


for example , the sequential computation in this case is

1+2=3
3+3=6
6+4=10                            the reduce function will return 10
 
'''



# another example of reduce function


l = [3, 8, 455, 2, 5, 45]

a = reduce(max, l)          # max(built-in function) function (remember max function will receive two arguments)is applied on list (sequential computaion will depend on max function now)
print(a)


'''
in above function, the sequential computation is followed as:


max(3,8) -> 8
max(8,455) -> 455
max(455,2) -> 455
max(455,5) -> 455
max(455,45) -> 455               # reduce function will return 455


 
'''





