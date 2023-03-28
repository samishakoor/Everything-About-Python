a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 123, 67]

# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# Shortcut to write the same:
b = [i for i in a if i%2==0]
print(b)


#example of list comprehension  (printing table of entered number in tables.txt file until user enters 0)

while True:
  num=int(input("Please enter a number: "))
  
  if(num==0):
      break
  table=[num*i  for i in range(1,11)]          # table list will contain the table of that number which is input by user


  with open("tables.txt","a") as f:         # append is the best way to write in a file 
      f.write(str(table))                   # write the table list in form of string in tables.txt file 
      f.write('\n')                         # cursor will move to next line
        


'''
if some elements/items repeats in a list
then we can remove the repeated elements 
by creating another list (using list_comprehension)
but remember the original list will not change
(means repeated elements will still present in original list)
but new list will not contain the repeated elements  
'''

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)

