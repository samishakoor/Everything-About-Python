l = []         # declaring an empty list

while True:
    c = int(input(''' 
           1. Push
           2. Pop
           3. Peek
           4. Display
           5. Exit
           '''))
    if c == 1:
      n = input('Enter the value: ')
      l.append(n)
      print(l)
    elif c == 2:
      if len(l) == 0:
        print("Empty Stack")
      else:
        p = l.pop()
        print(f"{p} is popped")
        print(f"new updated list is {l}")
    elif c == 3:
      if len(l) == 0:
        print("Empty Stack")
      else:
        print(f"Last value of stack is : {l[-1]}")
    elif c == 4:
       print("Display Stack")
       print(l)
    elif c == 5:
       break
