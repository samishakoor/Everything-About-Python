                    #Files and Directories

from pathlib import Path

#p=Path("Directories")        # now p targets Directories Folder
#print(p.exists())            # return true if Directories folder exists because p object targets the directories folder 

#p=Path("Emails")              #p is object of Path class pointing to Emails Folder
#print(p.exists())             #returns false because Emails Folder doesn't exist

#p=Path("Ecommerce")            # p is pointing to Ecommerce folder
#p.mkdir()                      #a new Folder of name "Ecommerce" will be made in that folder where this current python file is present

#p=Path("Ecommerce")            # p is pointing to Ecommerce folder
#p.rmdir()                      # Folder of name "Ecommerce" will be removed 

#path=Path();                        # path object is pointing to that location(path) where this current python file is present 
#for file in path.glob('*.*'):       #this will print all the files(not folders) names one by one which are present in that folder where this current python file is present
#    print(file)          

#path=Path();
#for file in path.glob('*.py'):      #this will print only those files(folders) names whose extension is 'py' one by one which are present in that folder where this current python file is present
#    print(file)
    
#path=Path();
#for file in path.glob('*'):      #this will print only those files and folders as well names one by one which are present in that folder where this current python file is present
#    print(file)



