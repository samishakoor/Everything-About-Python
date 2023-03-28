#A Dictionary is a collection of a key-value pairs
'''
Some Properties of Dictionaries:
1. It is unordered
2. It is mutable
3. It is indexed
4. It cannot contain duplicate keys

'''



myDict={
    "Fast" : "to run quickly",       # a simple key-value pair
    "Sami" : "a programmer",
    "Marks" :  [90,40,10],
    "anotherDict": {'player1':'sami','player2':'haseeb'},  #adding another dictionary as a key-value pair  i-e nested dictionary  
    1:3
}


print(myDict)            # simply print all the content as it is present in the dictionary
print(myDict['Fast'])
print(myDict['Sami'])
print(myDict['Marks'])
print(myDict[1])           #prints 3
print(myDict['anotherDict'])
print(myDict['anotherDict']['player1'])     #printing nested dictionary

myDict['Marks']=[20,80]       # changing/updating a key in a dictionary which means it is mutable
print(myDict['Marks'])


