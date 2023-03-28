l = []         # declaring an empty list

while True:
    c = int(input(''' 
           1. Push
           2. Pop
           3. Front Element (peek)
           4. Display
           5. Exit
           '''))
    if c == 1:
      n = input('Enter the value: ')
      l.append(n)
      print(l)
    elif c == 2:
      if len(l) == 0:
        print("Empty  Queue")
      else:
        del(l[0])
        print(f"new updated list is {l}")
    elif c == 3:
      if len(l) == 0:
        print("Empty Queue")
      else:
        print(f"Front value of queue is : {l[0]}")
    elif c == 4:
       print("Display  Queue")
       print(l)
    elif c == 5:
       break