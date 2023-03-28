# we can raise custom exception using raise keyword

def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")       # we raise ValueError (user's choice) to handle error if thrown by code in try block

a = increment('3fd64')
print(a)

