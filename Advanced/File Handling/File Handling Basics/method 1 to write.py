# writing to a file
f=open('sampleWrite.txt','w')       # if sampleWrite is not created by user then it will be automatically created
f.write("I am writing to a file\n")
f.write("I am  writing again")
f.close()

'''
 when we write some text in a file , that text is of string datatype i-e str
 so if we want to write an integer in a file , we need to convert that integer 
 in string as :

data=5;
f.write(str(data))                        # here the integer data is converted into str first then write into file

'''

