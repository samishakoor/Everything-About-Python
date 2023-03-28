'''
split function will take listname as an argument an split the list items by a specific given string/character and returns that splitted 
list in a string (original list is not affected)
'''


l = ["Camera", "Laptop", "Phone", "ipad", "Hard Disk", "Nvidia Graphic 3080 card"]


#sentence = "~~".join(l)          # join(listname) will seperate/split each item of list by '~~'  and convert the resulted/splitted list in a string 
#sentence = "==".join(l)        # join(listname) will seperate/split each item of list by '=='  and convert the resulted/splitted list in a string 
sentence = "\n".join(l)         # join(listname) will seperate/split each item of list by new line(each item of list is printed on new line)  and convert the resulted/splitted list in a string 
print(sentence)
print(type(sentence))                  # sentence is a string


print()



# another example

l = [str(i*7) for i in range(1, 11)]        # list 'l' will store the table of 7
print(l)

verticalTable = "\n".join(l)              # here, join function will split each element of list 'l' by a new line
print(verticalTable)                       # vertical table is a string



