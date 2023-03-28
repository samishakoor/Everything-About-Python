
class Point:                               # class name should be start with a capital letter
    def move(self):                        # a member function of class Point
        print("move");
    def draw(self):
        print("draw");                  # a member function of class Point

point_obj=Point();                  # point_obj is an object of class Point (just like (Point point_obj) in C++)
point_obj.x=10;                     # defining an attribute(member variable) p.s we can define an attribute anywhere we want
point_obj.y=20;
print(point_obj.x);                 #10                  
print();

                        #constrctor

class Point1:
    def __init__ (self,x,y):                      # defining a constructor
        self.x=x;
        self.y=y;
    def move(self):                       
        print("move");
    def draw(self):
        print("draw");                  

Point_obj=Point1(10,20);                  
print(Point_obj.x);                     #10
print();

                        #inheritance

class Mammal:
    def walk(self):
        print("walk");


class Animal(Mammal):      #Animal class is inheriting Mammal class
      pass            # pass means that there is nothing in this class
        

class Cat(Mammal):
    pass


animal_obj=Animal()
animal_obj.walk()                 # an object of Animal class is used to call the method of its parent class Mammal because of inheritance
