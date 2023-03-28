'''
'lambda' function  is a one liner function (can be considered as a shortcut function) which takes some arguments 
and returns a value
for example,

sum = lambda a, b, c: a+b+c           (here the name of lamcda function is 'sum')

in above lambda function,  before colon, a,b,c are the arguments which are passed to 'sum' function
and a+b+c is the one liner code which is returned so , we can say that sum function will return (a+b+c)
'''

'''
lambda function can take more than one argument but the code inside it (after colon) should be one line or simpler
'''


#example of lambda function

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c



x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6


#alternative of lambda function (when we open lambda function , it seems like this)

def func(a):
  return a+5


print(func(5))


