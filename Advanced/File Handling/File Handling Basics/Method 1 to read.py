'''
Modes of opening a file:
1. r -> open for reading   ( rb for reading in binary mood and rt for reading in text  mode )
2. w -> open for writing
3. a -> open for appending
4. + -> open for updating
'''


                             #Method #1

#open is a reserved keyword to open a file and close is used to close a file

# file=open('sampleRead.txt')             # by default the mode is r (read)
file = open('sampleRead.txt' ,'r')                 # r keyword means to read a file

data=file.read();                 # this will read the whole file     (when we read from file and store it in a variable (in this case we read file and store it in 'data' variable) then this variable is of string type(so the datatype of 'data' variable is str))
#data=file.read(5);               # this will read the only first five charaters in the whole text file


print(data);                     #displays text line by line

file.close()                    








#another example of replacing data in a file

#with open('sampleRead.txt') as f:
#    content=f.read()
    
#content=content.replace("donkey", "#####")
    
#with open('sampleRead.txt','w') as f:
#    content=f.write(content)