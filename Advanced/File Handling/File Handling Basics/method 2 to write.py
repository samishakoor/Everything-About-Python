# writing to a file 

#with keyword is used to open and close a file automatically , we dint need to open or close seperately
with open('sampleWrite.txt','w') as f:      # if sampleWrite is not created by user then it will be automatically created
  f.write("I am writing to a file using method 2")

# This method will also work on reading files