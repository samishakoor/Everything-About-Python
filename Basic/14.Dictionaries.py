 #Dictionaries (used to store key-value pairs)
        
customer = {            
     "Name": "Sami",                      #Name is key and Sami is value
     "age": 20,                           #age is key and 20 is value
     "is_verified": True                  #is_verified is key and True is its value
}

# we can add more key-value pairs to a dictionary and update it as well
customer["BirthDate"]="Jan 1 2002";      #now this key-value pair is also added to cutomer dictionary
# we can also add a dictionary in already created dictionary (nested dictionary)
customer["anotherDict"]="{'name':'sami','age':'20'}"

print(customer)


print(customer["Name"]);          #Sami
print(customer.get("Name"))       #Sami
print(customer.get("gender"));    #returns None because gender is not present in customer dictionery
print(customer.get("Brother Name","!"));    # it means that if Brother Name is not a included in customer dictionary , then "!" will be displayed in output but AT THE END 
print();

#example of dictionary

phone=input("Phone: ");           #taking input
digits_mapping={                  #declaring dictionary
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    }

output=""                        #declaring output as null 
for  ch in phone:
    output+=digits_mapping.get(ch,"!") + " ";       #if ch is not present in dictionary then ! is printed
print(output);



# converting dictionary into list

y=[x for x in customer]                # only keys from customer dictionary is added in the list
print(y)            




# nested dictionaries

course={
    'php':{'duration':'3 months','fees':'12000'},
    'java':{'duration':'4 months','fees':'16000'},
    'python':{'duration':'4 months','fees':'21000'}
}

print()

# observe the difference between the results of below 3 functions
for x,y in course.items():           # x will store the key and y will store the pair   and course.items includes all the dictionaries present in the course dictionary  
    print(x,y)

print()


for x,y in course.items():           # x will store the key and y will store the pair   and course.items includes all the dictionaries present in the course dictionary  
    print(x,y['duration'],y['fees'])

print()

for x,y in course.items():           # x will store the key and y will store the pair   and course.items includes all the dictionaries present in the course dictionary  
    print(x,y['duration'])

print()

