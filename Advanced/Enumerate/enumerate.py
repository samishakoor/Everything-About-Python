
            #Old method (without enumerate)

#list1 = [3, 53, 2, False, 6.2, "Harry"]
# index = 0
# for item in list1:
#     print(item, index)
#     index += 1


            #enumerate
#The enumerate function adds the counter to an iteration and returns it 
            
list1 = [3, 53, 2, False, 6.2, "Harry"]
for index, item in enumerate(list1):        # prints the items of list 1 with index as well
    print(item, index)
    
print()    
    
#another example of enumerate    
    
list2 = [3, 53, 2, False, 6.2, "Harry"]
for index, item in enumerate(list2):        # prints the items of list 1 with index as well
    print(f"The {index+1}th element is {item} ")
    

'''
so we can say , enumerate allows us to access the list elements  using their index
(remember the index of list starts from 0)
'''    

