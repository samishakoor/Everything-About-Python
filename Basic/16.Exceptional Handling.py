                      #Exception Handling

#example1
try:
    age=int(input('Age : '));         # let's assume we input abcd
except ValueError:
    print("Invalid Value");

#example2
try:
    age=int(input('Age : '));       # let's assume we input 0
    income=2000;
    risk=income/age;
except ZeroDivisionError:
    print("Age cannot be zero");