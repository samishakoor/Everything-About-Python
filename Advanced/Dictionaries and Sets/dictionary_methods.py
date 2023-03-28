myDict={
    "Fast" : "to run quickly",       # a simple key-value pair
    "Sami" : "a programmer",
    "Marks" :  [90,40,10],
    "anotherDict": {'player1':'sami','player2':'haseeb'},  #adding another dictionary as a key-value pair  i-e nested dictionary  
    1:3
}

#Dictionary Methods
#  1.getting keys
print(myDict.keys())      # prints all the keys(not their corresponding values) in myDict
#  2.getting values
print(myDict.values())    # prints all the values of all the keys(not print keys) in myDict
#  3.getting all the content in dictionary(i-e, all the key value pairs)
print(myDict.items())     # prints all the key-value pairs in the form of tuple and can be iterate-able (a kind of list but not actual list)
#  4. updating in the dictionary
updateDict={
    "Degree":"BSCS",
    "Roll no":21    
}
myDict.update(updateDict)          # updating the myDict dictionary using method
print(myDict)                      #printing the updated dictiona
#  5. getting a specific value in front of key
print(myDict.get("Fast"))            #prints value present in front of key named 'Fast'

# difference between myDict.get("Fast") and myDict['Fast']        
'''
Both are thesame ways to do the same thing but 
myDict.get("Fast") returns/prints "None" if
'Fast' key is not present in myDict dictionary.
On the other hand,  myDict['Fast'] throws an
error if 'Fast' key is not present in myDict dictionary.
But if Fast key is present then both myDict.get("Fast") and
myDict['Fast'] shows the same result.
'''

#in order to iterate the dictionary , myDict.items() is the solution
print(type(myDict.keys()))        # prints the type of dictionary which is class 'dict_keys'
 
#converting keys of dictionary into a list
print(list(myDict.keys()))    

#converting values of dictionary into a list
print(list(myDict.values()))   

#empty dictionary
fav={}              # an empty dictionary
print(type(fav))    # class 'dict'



