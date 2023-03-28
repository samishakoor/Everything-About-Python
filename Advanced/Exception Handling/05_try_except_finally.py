try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()           # when exit() executes , the program will be terminated and no code below exit() will run because we terminated the program 
finally:             # 'finally' block will run didn't matter exception is thrown(by try block) or not 
    print("We are done")

print("Thanks for using the program")


'''
when we use "finally" block in exception handling 
then it does not matter if exit() is written in code
or not , the finally block will always run 
'''


'''
code in finally block will run regardless of error.
if try block is successful , tab bhi 'finally' block chalay ga aur
agr try block se error throw hua tab bhi except block
chalnay ke baad 'finally' block chalay ga
'''

'''
agr 'finally' block na ho aur exception throw ho jaaye 
aur  exception block ma exit() likha ho to exit() ke baad program
terminate ho jaaye ga aur baaki ka jitna bhi code exit ke neeche 
likha ho ga wo nhi chalay ga (for example code at line no 10 will not execute),
lekin agr finally block bhi present ha aur exception bhi throw hui (try block se)
to exit() (jo k except block ma present ha) ke baad finally block zaroor chalay ga
'''