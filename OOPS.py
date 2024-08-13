#CLASS is a blue print for an object (entity) eg:- car ,animal,student.....
'''
class student:
    #define class variables (artributes)
    name=''
    age=0
    rollno=''
    dept=''

    stu_count=0 #class variable which is shared among all object

    #create a constructor method of the class
    #constructore is ised to initialize variables duirn gobject creation itself
    #constructor mehtod is airomatically invoked when the object is created
    #srats with __ and end swith __ its called a spcl method
    def __init__(self,name,age,rollno,dept):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.dept=dept
        student.stu_count += 1 #increment the common class variable with 1


    #define class functions
    #pass an identifier called self which holds the obj of the class
    def get_stud_details(self):
        print('\n\nName:',self.name,'\nAge:',self.age, '\nRoll no:',self.rollno,'\nDept:',self.dept)

    def get_total_stud_count(self):
        print("Total stud count is ",student.stu_count)

'''
#if not using the ocnstructors, we would have to add the values individulally
#access the artributes or propertires using the dot operator
'''
student1.name='Akash'
student1.age=22
student1.rollno='KTU1000'
student1.dept='CSE'
student1.get_stud_details()

student2.name='Preethi'
student2.age=22
student2.rollno='KTU1001'
student2.dept='CSE'
student2.get_stud_details()

'''

'''
#create object for this class
#syntax------> objname=classname()

student1= student('AKash',22,'KTU1000','CSE')
student2= student('Preethi',22,'KTU1001','CSE')

student1.get_stud_details()
student1.get_total_stud_count()

student2.get_stud_details()
student2.get_total_stud_count()

#INHERITANCE

class latstudent(student):
    def __init__(self, name, age, rollno, dept,sem_joined,course_done):
        self.sem_joined = sem_joined #Passing the additional varaiable into our class
        self.course_done = course_done
        student.__init__(self,name,age,rollno,dept)
        #call the parent class constrcutor to pass the rest of variables

    def get_sem_joined(self):
        super().get_stud_details() #to call main class methoda inside subclass methods isde super() method
        print('sem joined was ',self.sem_joined)

    def get_course_done(self):
        print('Course done was ',self.course_done)


#create pbject for our derived class

lat_student1=latstudent('Sanju',23,'KTU1002','ECE',3,'Polytechnique')

lat_student1.get_stud_details()
lat_student1.get_total_stud_count()
lat_student1.get_sem_joined()
lat_student1.get_course_done()





'''
'''
#ASSIGNMENT

class calculator:
        
        def __init__(self,num1,num2):
            self.num1=num1
            self.num2=num2

        def sum(self):
             print(f'{self.num1}+{self.num2}={(self.num1)+(self.num2)}')

        def multiply(self):
             print(f'{self.num1}*{self.num2}={(self.num1)*(self.num2)}')

        def divide(self):
             print(f'{self.num1}/{self.num2}={(self.num1)/(self.num2)}')

calculation1=calculator(10,2)
calculation2=calculator(40,3)

calculation1.multiply()
calculation2.divide()
'''

'''

#multuply inheritance - child calss can inherit from multiple parent class
#definign parent classs 1
class Animal:
    def print_animal_details(self):
        print('Creatures that can move in earth.')

#defining parent class 2

class WingedAnimals:
    def print_winged_animals_details(self):
        print('Animals that can fly over earth.')

#definig a child class that inherits from both parents

class Bat(Animal,WingedAnimals):
    pass #pass statement to make the block valud when we have no more statements


#creating an object of the child class
bat1=Bat()
bat1.print_animal_details() #funciton from parent 1
bat1.print_winged_animals_details() #function from parent 2

'''
'''
#Encapsulation - wrapping fata in a class so that direct access can be prevented

class corebanking:
    def __init__(self,cust_name,cust_ac_no=0):
        self.cust_name= cust_name
        self.__cust_ac_no=cust_ac_no
        #converting into provate so that direct access is not possible

    def get_name(self):
        return self.cust_name
    def get_ac_no(self):
        return self.__cust_ac_no #this var can be accesses onlu using this fn
    
cust1=corebanking('Tom',555555)
print(cust1.cust_name)
print(cust1.__cust_ac_no) #__cust_ac_no cannot be acceses, will show a error


print(cust1.get_name())
print(cust1.get_ac_no()) #the proper way to call 
'''
'''
#POLYMORPHISM
#METHOD OVERRIDING

#DEFINING A BASE CLASS

class shape:
    def __init__(self,shape_name) :
        self.shape_name= shape_name

    def find_area(self):
        pass

    def return_info(self):
        return 'I am a basic shape'
    
    def __str__(self):
        return self.shape_name #if we print the obj,it will print this value
    
#definign sub class

class Square(shape):
    def __init__(self, length):
        self.length= length
        super().__init__('Square')
        #since shape is inherited
    
    def find_area(self): # overriding the base class shaoe's find_area(),method
        return self.length**2

    def return_info(self): # overriding the base class shaoe's return_info(),method
        return 'I am square'

class Circle(shape):
    def __init__(self, radius):
        self.radius= radius
        super().__init__('Circle')
        #since shape is inherited
    
    def find_area(self): # overriding the base class shaoe's find_area(),method
        return 3.14*(self.radius**2)




#Create objects for a sub class
square1=Square(10)
circle1=Circle(5)

#printing the name using the __str__(self) in the base class

print(square1)
print(circle1)



#accessing the overridden method return_info()
print(square1.return_info()) #will print the overridden return infor from Square cls
print(circle1.return_info()) # This will print the non overridden return info from from the base class


#accessing the find area() function
print(square1.find_area()) #will print the overridden find_area() from Square cls
print(circle1.find_area()) # This will print the  overridden find_area() from from the base class

#we can also loop through the methods using simple for loop

for shape in (square1,circle1):
    print(shape.find_area())
    print(shape.return_info())

'''

'''
#operatoroverloading, same operator to have different meaning
#we trying to overload teh + operator so thet it can add 2D co-ordinatees
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#special string fn to print the object in our prescribed format of (x,y)
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)

#defining the special functions to overload the add operator
#p1.__add__(p2) is equivalent to p1 + p2
    def __add__(self, second_point):
        x = self.x + second_point.x
        y = self.y + second_point.y
        return Point(x,y) #return sum as an object of point class

#creating two point objects
p1 = Point(1,2)
p2 = Point(3,4)

print(p1+p2)

#we usually decorate a normal out of class fn using @symbol on top of the fn
#we can also decorate the class methods (functions) mainly in 3 ways

#1. using the built-in classmethod decorator
class Hero:
    @classmethod
    def say_hello(cls):
        #checking the class name of the inherited class var __name__
        if cls.__name__ == 'HeroSon':
            print("Hello dear Prince Charming...")
        elif cls.__name__ == 'Hero Daughter':
            print("Hello Gorgeous Cindrella...")    

#Heroson inheriting Hero class
class HeroSon(Hero):
    pass #just creating an empty class

class HeroDaughter(Hero):
    pass

hero_son1 = HeroSon()
hero_son1.say_hello()

hero_daughter1 = HeroDaughter()
hero_daughter1.say_hello()

#2. using the built-in staticmethod decorator
class Hero2:
    @staticmethod #decorating the method with staticmethod decorator
    def say_hello():
        print("Hello")

#we cannot access the staticmethod decorated fn using the obj instance
#we can directly access it,
Hero2.say_hello() 
'''
'''
#3. using the built in  property decorator
# to ensure safety of the variable (attribute)
#declaring some of them as protected(with apreceeding underscore_)
#so thet tghis attribute is not accessible directly or by creating an obj
#we need tocreate getter() setter() and deleter() methods to operatre on them.

class House:
    def __init__(self,price):
        self.price = price #making the price attribute protected using underscore
    #create a getter method (to get the value) using the @property decorator
    #make sure the name is the sum as thet of the attribute
    #and the decorator is @property
    @property
    def price(self):
        return self._price
    
#create a setter method (to set the the value) using the atrributename.setter
# #make sure the attributename is the same as that of the attribute
 
    @price.setter
    def price(self, new_price):
        self._price = new_price

#create a deleter method (to delete the the value) using the atrributename.deleter
# make sure the attributename is the same as that of the attribute
 
    @price.deleter
    def price(self):
        del self._price 



print(House.price)  #ERROR - cannot access directly
house1 = House(5000)
print(house1.price)
house1.price = 10000
print(house1.price)
del house1.price
print(house1.price)


'''
'''
#Abstract based class
#if you declarea  class as an abstract class,every  child class tha inherits
#that bse class should implement all the abstract methods from that base class

from abc import ABC , abstractmethod #import the ABC class and the decorator

#creating the abstract base class by inheriting the ABC class
class Animal(ABC):
    @abstractmethod
    def feed(self,fav_food): #define the abstract method by usin gthe dcorator @abstractmethods
        pass #will write the code later

    @property #to define an abstract variable, we musr use @poperty and @abstractmethod
    @abstractmethod    #that is if we use prooeryt and abstract method, it acts as a variable,not a method
    def favorite_food(self): # we can only return a value or print a calue, we cannot do any other function in side the property ,asntract
        pass


    def sleep(self):
        print('Sleeping')

#now all the sub classes that in herits the abstract base class should 
#implement the @abstractmethos decorated function

class lion(Animal):
    @property
    def favorite_food(self):
        return 'Rabbit meat'

    def feed(self,fav_food,time): #this method should be defined (IMplemented) as mandatory
        print(f'Feedign the lion with {fav_food} at {time}.')

    
    def roar(self):
        print('Roaring..')

class panda(Animal):
    @property
    def favorite_food(self):
        return 'Bamboo twigs'

    def feed(self,fav_food,time):
        print(f'Feeding panda with {fav_food} at {time}.')

#creating gthe objects for all class in a single line as an iterable
zoo_animals = [lion(),panda()]
#now we can easily loop thorugh the absract methods of objects using fro loop
for zoo_animal in zoo_animals:
    zoo_animal.feed('Apple','10:00 AM')



#or we can create individual objejcts and call the function

simba=lion()
kungfupanda=panda()

simba.feed('Mutton','9:00 AM')
kungfupanda.feed('Bamboo leaves','10:00 AM')

'''
'''
#ASSIGNMENT ABSTRACT CLASS
from abc import ABC , abstractmethod #import the ABC class and the decorator

class calculate(ABC):
    
    def num1()

    @property
    @abstractmethod 
    def performcalculation(self,num1,num2):
        pass

class sum(calculate):
    @property
    def performcalculation(self,num1,num2,oper):
        return self.num1+self.num2

class diff(calculate):
    @property
    def performcalculation(self,num1,num2,oper):
        return self.num1-self.num2

class divide(calculate):
    @property
    def performcalculation(self,num1,num2,oper):
        return self.num1/self.num2
        
class product(calculate):
    @property
    def performcalculation(self,num1,num2,oper):
        return self.num1*self.num2



num1=int(input('\nEnter the number 1:'))
num2=int(input('\nEnter the number 2:'))
oper=input('\nENter the operation:')


calculation1=calculate(num1,num2,oper)


print(calculation1.sum(num1,num2))

'''
'''
#HIGHER ORDER FUNCTION

#1.map() - can apply a function to each and every element of  an iterable

#definin a simple function to fin d square of a number

def find_square(mynum):
    return mynum*mynum


#define the map function so that we can fine the square of each and every
#element in a tuple and rerturn back the processed tuple
#syntax: map(function,iterable)

my_tuple=(1,2,3,4)
result_map_obj=map(find_square,my_tuple)
print(tuple(result_map_obj))

#implementing map() fn with lambda functions

result_map_obj=map(lambda num: num*num , my_tuple)

print(tuple(result_map_obj))


#2.filter function
#that return true on condition
def find_square(mynum):
    return mynum*mynum





#3.Reduced function
#fn to apply a fn to the iterable and reduce 
def add_numbers(num1,num2):
    return num1+num2

from functools import reduce
my_tuple=(1,2,3,4)
result_map_obj=reduce(add_numbers,my_tuple)
print(result_map_obj)

#implementing map() fn with lambda functions

result_map_obj=reduce(lambda num1,num2: num1+num2 , my_tuple)

print((result_map_obj))

'''

#Execption handling in python using try execpt else finally statementsa
#here we are trying to open a non existing file and will handle the exeption

try:
    file=open('somefile.txt')
    try:
        file.write('some content')
    except:
        print('Writing cannot be completed')
    finally:
        file.close()
except:
    print('The file cannot be opened')
finally:
    print('Lets move on witht he program')










































































































































































































































































































































































































































































































































































































































































































