#print("HEllo world!!")
#print("hello inapp")

#this is a sungle line comment
'''
this is a 
multi line 
comment
'''
'''
#CASE SENSITIVE

#VARIABLE EXAMPLES
#follow intentation

message='good morning'
print(message)

#number variable
my_money = 100 # integer
my_balance = 1000.95 # float

num1 = num2 = num3 = 5 #MULTIPLE ASSIGNMENTS,signle values for all variables

num1,num2,num3,my_name = 5,10,15,'vijay' # assign multple values to all variables

print(my_money,my_balance,num1,num2,num3)

num1= num1+2
print(num1)


del my_money

my_str="200" #this is a stirng
my_int = int(my_str) # covert to a int and storing in a different variable
print(type(my_int))

my_int = float(my_str) # covert to a float and storing in a different variable
print(type(my_int))

my_str = str(my_int)
print(type(my_str))

#when converting a string to integer, make sure it contain all integers

#mathematical operators

print(my_int+my_int)

print(my_int-my_int)

print(my_int/my_int)

print(my_int%my_int)

print(my_int ** 2) # ** is used for a raised to operator


#STRINGS

print('A Sample string')
print('hello world')
print("hello world and 'hello you' for you ")

my_text="good moring world"
print(my_text)

print(my_text.upper())
print(my_text.lower())
print(my_text.title())

#adding special chars fto stirng like \n for new line and \t for tab

print("how\tare\tyou\nfine")

my_str = "    good day    "
#using Lstrip ,rstrip and strip


print(my_str.lstrip())
print(my_str.rstrip())
print(my_str.strip())

'''

'''
greet='Good morning'

print(greet)
print(greet[0])# only letter 0
print(greet[2:5])#from letters 2 to 5
print(greet[2:])# from letters 2 to full
print(greet * 2)#displays 2 times
print(greet + ' how are you') #concatnate

# STRING FORMATING METHODS

#F-STRING FORMATING

make='DELL'
dollar_rate=80.25;

mytext=f'The amount for this {make} computer is %d USD \
 and the exchange rate is {dollar_rate} USD'

print(mytext)

#fromat using % operator
mytext='The amount for this %s computer is %d USD  and the exchange rate is %4.2f USD' %(make,1200,dollar_rate)
print(mytext)

#format using format()
mytext='The amount for this {0:s} computer is {1:d} USD  and the exchange rate is {2:4.2f} USD' .format(make,1200,dollar_rate)
print(mytext)

#count()

print('hellow good morning'.count('d'))
print('hellow good morning'.count('d',3))
print('hellow good morning'.count('o',3,13))

#endswith('man')

'''
'''
#few more string manpualtion methods
#count() cuuting the number of occurances if a substring 

print('hello good morning'.count('o'))
print('hello good morning'.count('o',5)) # counts the nuber of o from 5th index
#print('hello good morning'.count('o',5,8)) # counts the nuber of o from 5th index till 8th index

#endswith() to check if its ends with a particular substring

print('Superman'.endswith('man'))
print('Superman'.endswith('sper'))

print('Superman'.endswith('man',3))
print('Superman'.endswith('man',6))

print('Superman'.endswith('ma',3,7))

print('Superman'.endswith(('ma','man'),3,7))



#find() and index() function to find the first occurance index of a substring

#find() will return -1 if not found and index() will return a error


print('hI Good Morning Go'.find('Go')) #return the first occurance of Go
print('hI Good Morning Go'.find('man')) # return -1 for since it doesn't include that
print('hI Good Morning Go'.find('Go',2,12))

print('hI Good Morning Go'.index('Go',2,12))

# print('hI Good Morning Go'.index('xx',2,12)) # shows erroe since it doesn't havae xx

#isalnum() will return true if the string is alphanumeric string

print('hello2024'.isalnum())

print('hello 2024'.isalnum()) #space is considered as special character so return false

print('2024'.isnumeric())

print('hello 2024'.islower())


#join()

seperator='***'
mytuple=('India','is','my','country')

print(seperator.join(mytuple).lower())

print(seperator.join(mytuple).upper())

print('hello 2024'.isdigit())

print('hello'.isalpha())


#replace() to replace a subsstring ina astring with another string
print('hellow world'.replace('hellow','Hi'))

print('hellow world hellow how are you hellow finw'.replace('hellow','Hi',2))

#split() to split using a deliminator and polace the fragments in a list
mylist='Hello world how are you'.split(' ') 
print(mylist)


#PATTERN SEARCH USING REGULAR EXPRESSIONS
#REGULAR EXPRESSION FUNCTION ARE AVAILABLE AT RE MODULE

import re
mystring='bits of paper bits of paper'
#using the findall function
occurence=re.findall('bi',mystring)
print(occurence)

#using the findall function
occurence=re.search('bi',mystring)#return back a search object
print(occurence.span()) #return a tuple with start and end pos of the match
print(occurence.group())#return the part of the string whre rhwew was a match
print(occurence.string)#return the actual string
print(occurence)

#using the sub function for substritution

substituted_string = re.sub(' ','*',mystring) #return the substitured string
print(substituted_string)

#using th esplit fucntoin for spliting string 
splits = re.split(' ',mystring) #return the splitted list
print(splits)
'''
'''
import re
#Pattern search using metachars
#[] will search a set of chars or a range of chars in a string

mystring="HEllo World"
matches=re.findall('[a-m]',mystring)
print(matches)

# \ used to denote a special sequence 

mystring='i will give you 100 rupees'

matches=re.findall('\d',mystring) # finidng all integers
print(matches)

# . used to find any characters exepect new line characters(\n)
matches=re.findall('ru...s',mystring)
print(matches)

# ^ sysmbol is used to check for strating of an entire string
mystring='hello world'
matches=re.findall('^hello',mystring)

# $ for checking end of a a entire string
mystring='hello myworld yourworld'
matches=re.findall('world$',mystring)
print(matches)

#\A similar to ^ for checking if the entire starting with the given string
mystring='hello world'
matches=re.findall('\Ahello',mystring)
print(matches)

#we can search boundry using \b

mystring='radha vinu and manu are anumy good anufriends'

# \b in the left to search for all words starting with
matches=re.findall(r'\banu',mystring)
print(matches)


# \b in the right to search for all words ending with
matches=re.findall(r'friends\b',mystring)
print(matches)

# \b in the beginning and end of a word with exact match
matches=re.findall(r'\bgood\b',mystring)
print(matches)

# \s to search for all non space chars expet space
mystring='hi my email is test@test.com please do send mail'

#to find all email addresses in the string
#starting with some non sapce string, then an @ , then some non space string

matches=re.findall(r'\S+@+\S+',mystring)
print(matches)

'''
'''
#collection in python
#LISTS
#accessing the list items by index numbers

studentsage=[18,21,23,50,56]
print(studentsage[2])

#List access oprion

print(studentsage[-1])#gets the last element
print(studentsage[-2])#gets the second last
print(studentsage[2:3])#resturn a lis sliced from original from 2 ro 5
print(studentsage[2:]) #return a list frm 2 to end
print(studentsage[::-1]) #reverse the list

studentsage.append(20) # adds 20 to the end
studentsage.append('hi') # adds hi to the end
print(studentsage)

del(studentsage[5]) # delete the 5th index element\
print(studentsage)

greeting=['h','e','llo']
studentsage.extend(greeting)# adds content in greeting to the end od studentsage
print(studentsage)


print('llo' in studentsage) # return true if it exists there
print(len(studentsage)) #returns the length of the list

studentsage.reverse() #will reverse the actual list

print(studentsage)

mylist=['ddd','fff','kkk','wdsq','wefw']

mylist.sort() #list has to be in a single data type

print(mylist)

#list addition and multiplication

print(mylist+mylist) # adds two list
print(mylist*3)# return the 3 times of the list in a single list


'''
'''
#TUPLE
#WE CANT EDIT OR CHANGE THE ELEMENTS IN ATUPLE
#WE CAN ONLY FULLY CHANGE OR FULLY DELETE THE TUPLE
months=('jan','feb','mar','apr','may','jun')

print(months[0])
print(months[-1])

print(len(months))

print('jan' in months)

newmonths=months+('jul','aug','sep')
print(newmonths)
newmonths=months=months*2

print(newmonths)

del newmonths

'''
'''
#DICTIONARY

#COLLECTION OF KEY VALUE PAIR
myStudents = {'Akash':1000,'JD':1001,'Sanju':1003,'SUSMIN':'Not defined'}
print(myStudents)

#OR

myStudents=dict(Akash=1000,JD=1001,SANJU=1002,SUSMIN='Not defines')
print(myStudents['Akash'],myStudents['SUSMIN'])
myStudents['SUSMIN']=1004

print(myStudents.get('JD'))

print(myStudents.items())

print(myStudents.keys())

print(myStudents.values())

print(1003 in myStudents)

print(len(myStudents))

mynewstudents={'Meenakshi':1000,'Arunima':1005,'Akash':1100}

myStudents.update(mynewstudents) #REPLACE EXIXSTING AND ADDS NEW VALUES

print(myStudents)

mynewstudents.clear() #Clear the content inside the dictionary
print(mynewstudents)

del mynewstudents

------------------------------------------------------------------------------------------------
#SET - collection of unordered items
#each element has to be unique and no index


mystudents={'prethi','keerthana','sanju','sanju','susmin'} #DUPLICATE VALUE WILL BE DISCARDED

print(mystudents)

mystudents=set(['preethi','keerthana','sanju','sanju','susmuin'])
print(mystudents)

print(type(mystudents))

for student in mystudents :
    print(student)
mynewatudents=set() #will create new set

mystudents.add('Akash')
mystudents.add('Arunima')
mystudents.add('JD')
mystudents.add('Devika')

for student in mystudents :
    print(student)

#add multiple items at once,using update function

mystudents.update(['Tom','Jerry'])
print(mystudents)

#remove items using discard() or remove() funciton

#discard will nor hiev error if the item does not exists,but remove will

mystudents.discard('Tom')
print(mystudents)

#mystudents.remove('Donald') #shows error since it doesnt exixsts

mystudents.clear()
print(mystudents)

#SET OPERATIONS

MYSTUDENST1={'preethi','akash','keeerthana','sanju','sanju','susmin'}
MYSTUDENST2={'akash','devika','keerthana','JD','arunima','meenakshi'}
MYSTUDENST3={'preethi','akash'}
#UNION

print(MYSTUDENST1.union(MYSTUDENST2))
print(MYSTUDENST1 | MYSTUDENST2)


print(MYSTUDENST1.intersection(MYSTUDENST2))
print(MYSTUDENST1 & (MYSTUDENST2))

print(MYSTUDENST1.difference(MYSTUDENST2))
print(MYSTUDENST1 - (MYSTUDENST2))

#symmetric difference operation
print(MYSTUDENST1.symmetric_difference(MYSTUDENST2))


print(MYSTUDENST1>(MYSTUDENST2)) #check if mystd1 is a superset of mystd 2

print(MYSTUDENST1<(MYSTUDENST2))

print(MYSTUDENST1==(MYSTUDENST2))

#FROZEN SET
MYSTUDENST4=frozenset(['JD','Arunima'])

#MYSTUDENST4.add('Devika') # showserror sicne frozen set cannot be edited

MYSTUDENST1={'preethi','akash','keerthana','tom'}
MYSTUDENST2={'akash','devika','keerthana'}
MYSTUDENST3={'preethi','akash'}

MYSTUDENST1 .intersection_update(MYSTUDENST2,MYSTUDENST3)

print(MYSTUDENST1)

-------------------------------------------------------------------------------------------
'''
#EXPRESSION

#INPUT AND OUTPUT FUNCTIONS

#INPUT() FN TO GET INPUT FROM USER
#INPUT FUN ALWAYS STORES THE VALUE AS A STRING
'''
studname = input('Enter student name:')
studage = input('Enter student age:')

print(The student name is {} and his age is {}.format(studname,studage))



print("This is the frist line \n This is the next line.")

print('\nthis is a back slash \\')

print('My height i 5\'5')

#CONTROL FLWO STATEMENTS




if USERINPUT == '10':
    print("You enter 1.")
elif USERINPUT=='2':
    print('you entered two')
else:
    print('you didnt enter either one or two.')


USERINPUT = input("Enter either 1 or 2:")
print('you entered 1' if USERINPUT == '1' else 'you entered sonethig else')


#python does not have a switch case, instead it have a match case
#we should define the match case inside a function


def http_status_msg(status)
    match status:
        case 400:
            return 'Bad Request'
        case 401:
            return 'Unauthorised'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not Found'
        case _:
            return 'Some Other Error'

status_msg=http_status_msg(404) # calling the function http_status func
print('The status msg is',status_msg)

month=int(input("Enter month number from 1-12(Jan-dec)"))
if (month==1):
    print('GEM:-Garnet \n Bold and Alert.')
elif month==2:
    print('GEM:Amethyst\n Lucky and Loyal.')
elif month==3:
    print('GEM:Auamarine\n Naughty and Genius.')
elif month==4:
    print('GEM:Diamond\n Caring and strong.')
elif month==5:
    print('GEM:Emarald\n Loving and practical.')
elif month==6:
    print('GEM:Alexandrite\n Romantic and curius.')
elif month==7:
    print('GEM:Ruby\n adventurous and honest.')
elif month==8:
    print('GEM:Peridot\n Active and Hardworking.')
elif month==9:
    print('GEM:Saphire\n Sensitive and Pretty.')
elif month==10:
    print('GEM:Tourmaline\n Stylish and Friendly.')
elif month==11:
        print('GEM:Citrine\n Nice and Creative.')
elif month==12:
    print('GEM:Zircon\n Confident and Freedom Loving.')

#MATCH CASE
def DOBMONTH(MONTH):
    match MONTH:
        case 1:
            return 'GEM:-Garet \n Bold and Alert.'
        case 2:
            return 'GEM:-Amethyst \n  Lucky and Loyal.'
        case 3:
            return 'GEM:-Aquamarine \n  Naughty and Genius.'
        case 4:
            return 'GEM:-Diamond \n  Caring and strong.'
        case 5:
            return 'GEM:-Emarald \n  Loving and practical.'
        case 6:
            return 'GEM:-June \n Romantic and curius.'
        case 7:
            return 'GEM:-Ruby \n  adventurous and honest.'
        case 8:
            return 'GEM:-Peridot \n  Active and Hardworking.'
        case 9:
            return 'GEM:-Saphire \n  Sensitive and Pretty.'
        case 10:
            return 'GEM:-Tourmaline \n Stylish and Friendly.'
        case 11:
            return 'GEM:-Citrine \n  Nice and Creative.'
        case 12:
            return 'GEM:-Zircon \n People born in January are lovely.'
        case _:
            return 'ENTER A VALID MONTH'

MONTH=int(input('Enter Month Number:'))
details=DOBMONTH(MONTH)
print(details)


#LOOPS
fruits = ['Apples','Oranges','Banana','Cherry']
for fruit in fruits:
    print(fruit)


for indexx,fruitn in enumerate(fruits):
    print(indexx,fruit)


#Generate iterable list using range() fn and use for loop
for mynum in range(0,100,5): #start at 0, end at 100-1,step size of 5
    print(mynum)

#WHILE
total_num=50
while total_num>40:
    print('my_num=',total_num)
    total_num=total_num-1



counter = 10

while counter >2:
    if counter==6:
        break
    print('counter is now at=',counter)
    counter=counter-1

print('loop exited after continue')


while counter >2:
    if counter==6:
        continue     #skips that particular itereation                  
    print('counter is now at=',counter)
    counter=counter-1


try:
    answer=12/0
    print(answer)
except:
    print('An error occured')



for multiple in range(2000,2501,1):
    if multiple%8==0 and multiple%5==0:
        print('Divisible by 5 & 8:',multiple)


X=int(input('Enter a number from 1-10:'))
for i in range(1,11,1):
    mul=i*X
    print('{}*{}={}'.format(X,i,mul))
    


#LIST COMPREHENSION,creating a new list from a existing list based on a condition

#normal code without comprehension
words=['hello','world','how','are','you']

newwordlist=[] #our new empty list
#using a loop to save the words with O in it.
for eachword in words:
    if 'o' in eachword:
        newwordlist.append(eachword)
print(newwordlist)

#USING LIST COMPREHENSION IT CAN BE DONE IN A SINGLE LINE
#SYNTAX: NEWLIST=[exp for eachitem in items if condition(opt)==True]

newwordlist=[eachword for eachword in words if 'o' in eachword]
print(newwordlist) #same outputcan be generated in 2 lines

#with a expression
newwordlist=[eachword.upper() for eachword in words if 'o' in eachword]
print(newwordlist) #same outputcan be generated in 2 lines

#with conditional expression
newwordlist=[eachword if eachword !='hello' else 'hi' for eachword in words ]
print(newwordlist) #same outputcan be generated in 2 lines

newwordlist=['hello' for eachword in words]
print(newwordlist) #same outputcan be generated in 2 lines

newwordlist=[eachnum for eachnum in range(20) if eachnum<15]
print(newwordlist) #same outputcan be generated in 2 lines

upper=int(input('Enter upper year:'))
lower=int(input('Enter lower year:'))
newlist=[]
for i in range(lower,upper+1):
    if(i%4==0 or i%400==0):
            if(i%100!=0):
                newlist.append(i)
print(newlist)




#FUNCTIONS which can be defined with a name
#use camel name for function name,start with small case
def findSum(num1,num2):
    sum=num1+num2
    return sum

#calling the function
mysum=findSum(5,2)
print(mysum)

#to find if the number is prime or not

def check_if_prime(num1):
    for i in range(2,num1):
        if(num1%i==0):
            return False
    return True


print(check_if_prime(56))



#Assignment

barePrice=int(input('Enter the bare price(W/O tax):'))
tax=int(input('Enter the GST tax percent:'))

def price_calculation(barePrice,tax):
    realprice=((tax/100)*barePrice)+barePrice
    GST=(realprice-barePrice)
    CGST=(GST)/2

    print('Total Price={}'.format(realprice))
    print('GST={}'.format(GST))
    print('CGST={}'.format(CGST))
    print('SGST={}'.format(CGST))
    

price_calculation(barePrice,tax)


#FUNCTONS RETURNING MUKTIPLE VALUES
#RERTURNING MUKLTIPLE VALUES USING THE RETURN STATEMENT

def calculations(num1,num2):
    sum=num1+num2
    diff=num1-num2
    product=num1*num2
    divided=num1/num2
    return(sum,diff,product,divided)


#function calling
outputs=calculations(100,50)

#to get each value using the index of the list

print('Sum is ',outputs[0])
print('Difference is ',outputs[1])
print('Product is ',outputs[2])
print('Quotient is ',outputs[3])


#using yield we can convert thus fn into a generator fn
def calculations(num1,num2):
    sum=num1+num2
    yield sum
    diff=num1-num2
    yield diff
    product=num1*num2
    yield product
    divided=num1/num2
    yield divided

for value in calculations(100,50):
    print(value)

'''


'''
#VARIABLE SCOPE IN PYTHON'
#GLOBAL VARS ARE DECLARED OUTSIDE ANY FUNCTION,IN YHE MAIN PROGRAM COURSE
#LOCAL VARS ARE DECLARED INSIDE A FUNCTION AND CAN BE ONLY ACCESSED INSIDE THE FUNCTION



def my_function():
    print("I am inside the fn")
    print("printing global variable:",my_global_variable)
    my_local_var='I am a local var' #Local var declared inside function
    print("Printing local var:",my_local_var)

my_function()
#print('Printing local variable outside fn:',my_local_var) # gives error

print('Printing global variable outside fn:',my_global_variable) # gives error

my_global_variable='I am a global variable' #outside all the functions
print(my_global_variable)
#WE cannot edit a global variable inside a function
#to edit we use a global keyword inside the function

def my_function():
    global my_global_variable #niw you can change the value of a global variable
    print("I am inside the fn")
    print("printing global variable:",my_global_variable)
    my_local_var='I am a local var' #Local var declared inside function
    print("Printing local var:",my_local_var)
'''
'''
#PASSING ARBITARY LIST TO FUNCTIONS WHEN WE DONT KNOW THE NUMBER OF ARUGUMENTS WE ARE PASSIING
def make_pizza(crust_size,*toppings):              #preufx * for arbitary variable
    print(f'Making a {crust_size}- inch pizza with toppings:')
    #loop thorugh the arbitary list
    for each_toppings in toppings:
        print(each_toppings)


make_pizza('16','EXTRA CHEEZE','PEPPERONI','MUSHROOM','GREEN CHILLI')

#TO PRINT THE INGREDIENTS IN A LIST WITH 1,2,3
def make_pizza(crust_size,*toppings):              #preufx * for arbitary variable
    print(f'Making a {crust_size}- inch pizza with toppings:')
    #loop thorugh the arbitary list
    for index,each_toppings in enumerate(toppings):
        print(f'{index+1}:{each_toppings}')


make_pizza('16','EXTRA CHEEZE','PEPPERONI','MUSHROOM','GREEN CHILLI')
'''
'''
#TO pass keyword along with the argument
def make_pizza(crust_size,**toppings):              #preufx ** for keyword arbitary variable
    print(f'Making a {crust_size}- inch pizza with toppings:')
    #loop thorugh the arbitary list
    for each_layer,each_toppings in toppings.items():
        print(f'{each_layer}:{each_toppings}')


make_pizza('16',baselayer='EXTRA CHEEZE',middlelayer='PEPPERONI',toplayer='MUSHROOM')


#TO pass an argument , an arbitary argument and a keyword argument together
def make_pizza(crust_size,*crustype,**toppings):              
    print(f'Making a {crust_size}- inch pizza with following crust types and toppings:')
    #for loop for a arbitary arugument
    for index,each_crusttype in enumerate(toppings):
        print(f'{index+1}:{each_crusttype}')


    #For loop for keyword arguement
    for each_layer,each_toppings in toppings.items():
        print(f'{each_layer}:{each_toppings}')


make_pizza('16','thin','thick',baselayer='EXTRA CHEEZE',middlelayer='PEPPERONI')

'''
'''
def myfunction(operation,*numbers):
        
        if(operation=='+'):
            out=0
            for num in numbers:
                out=out+num
        if(operation=='-'):
            out=0
            for num in numbers:
                out=num-out
        if(operation=='*'):
            out=1
            for num in numbers:
                out=out*num


        print(f'final out after {operation} operation is {out}')


myfunction('-',3,4,5)


def myfunction1(operation,*numbers):
        
        if(operation=='-'):
            diff=0
            
            for num in numbers:
                diff=num-diff
                
        print(diff)
myfunction1('-',3,4,5)



#KEYWORD ARGUMENTS

def print_my_details(name,age,location):
    print('NAme:',name)
    print('Age:',age)
    print('Location:',location)

print_my_details('Tom',32,'TVM') #calling without keyword arguments,ie the arguments should be in same order
print_my_details(location='TVM',name='TOM',age=5) #we can pass arguments in any order ith the ise of the keyword

#LAMBDA FUNCTION, the function can be defined ina single line

sum= lambda num1,num2 : num1+num2
area= lambda len,bre : len*bre


print('Sum of numbers is:',sum(10,11))
print('Area of rectangle is:',area(10,11))

'''

'''
#ASSIGNMENT PHONE DIRECTRY
contacts = {'AKASH':'100100','DEVIKA':'1001223','SANJU':'100334','SUSMIN':'9237472','PRETHI':'927347923','ARUNIMA':'9434934','MEENAKSHI':'927347','KEERTHANA':'927349723','JD':'654469449'}

def listall(contacts):
    print(sorted(contacts.items()))

def addnew(newnumber):
    global  contacts    
    key=input('Enter the Name of the contact:')
    value=input('Enter the phone number of the contact:')

    newnumber[key]=value
    contacts = newnumber
    print("\nTHE CONTACT IS ADDED SUCCESFULLY.\n")

def delete():
    global contacts
    deletecontact=input('Enter the Name to delete:')
    del contacts[deletecontact]
    print('\nTHE CONTACT SUCCESFULLY DELETED.\n')

def searchbyname():
    name=input('Enter the name to search:')
    name=name.upper()
    for key in contacts:
        if(key==name):
            print(contacts.get(key))

def searchbynum():
    num=input('Enter the number to search:')

    for key,value in contacts.items():
        
        if value == num:
            print("\nThe required contact is ",key)


while True :
    
    print("\n\nPHONE DIRECTORY MENU\n")
    print("1.LIST ALL CONTACTS\n2.ADD NEW CONTACT\n3.DELETE A CONTACT\n4.SEARCH BY NAME\n5.SEARCH BY NUMBER\n6.EXIT PHONE DIRECTORY")
    action=int(input('\nEnter the option:'))
    if(action==1):
        listall(contacts)
    if(action==2):
        addnew(contacts)
    if(action==3):
        delete()
    if(action==4):
        searchbyname()
    if(action==5):
        searchbynum()
    if(action==6):
        exit()

'''

'''

#Function as first class objects
#functions are treated like a variable in python

def myfunction():
    print('This is just a function')

#assigning function to a variable
my_function_var=myfunction

#calling the function
myfunction() #CALL DIRECTLY
my_function_var() #CALL THE FUNCTION VARIABLE

#2. PASSING FUNCTION TO ANOTHER FUNCTION
def myfunction1():
    print('this is just a function1')

def myfunction2(var_to_hold_fn):
    var_to_hold_fn()

myfunction2(myfunction1)


#3.we can define function inside another funtion
def outer_fn():
    print('Inside outer funtion')

    def inner_fn():
        print('Inside the inner function')
    inner_fn() # Calling inner funtion inside the outer funtion
outer_fn()#calling the outer function

#4. returning a function from another function
def outer_fn():
    print('Inside outer funtion')

    def inner_fn(mytext):
        print('Inside the inner function,the text is',mytext)
    
    return inner_fn() # returning the inner function

my_outer_fn_var=outer_fn()
print(my_outer_fn_var('The value for my text'))

#5.inner funtoi ncan access outer funtion variables
def outer_fn(var_recieved_from_outer_fn):
    print('Inside outer funtion',var_recieved_from_outer_fn)


    def inner_fn():
        print('Insode the inner function',var_recieved_from_outer_fn)

    return inner_fn()

outer_fn_var=outer_fn('Good Evening')
outer_fn_var()


'''
'''
#moudules in python used to extende the functionaloty of the language
#import modles by using the ocde 'import modulesname

#give alias name to module by using the code 'import modulename as alias name'


#RANDOM
import random 

print(random.random())
print(random.randint(1,10))

mylist=['apple','bananna','cherry']
print(random.choice(mylist))

random.shuffle(mylist)

print(mylist)

#to generate random number the system will be pickin ga rando mnumber and do a calculation on that.
#if we use a seed we can fix the starting of the random selection or we can make the random number a constatnt for cheking purpose

print(random.randrange(1,20,2))

'''
'''
#PYTHON TIME MODULE
import time

print(time.time()) #print no of ticks from jan 1 1970

#get the current local tim ein tuples (yr,month,day,hr,min,sec,weekday,yearday,day1)

print(time.localtime(time.time())) #

print(time.asctime(time.localtime(time.time())))

for i in range(0,100
    print(i)
    time.sleep(2)           
    
'''
'''
#datetime module

import datetime
print(datetime.datetime.now())


mydate=datetime.datetime(2019,12,5)
print(mydate)

mydate=datetime.datetime(2019,12,5,9,30,0)
print(mydate)


if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,18):
    print("Working hours.")
else:
    print("Shift completed.")

#calender
import calendar
#creating a calender object
my_calender=calendar.month(2024,8)
print(my)


import math

print(math.fabs(-10.25))
print(math.pow(3,2))
print(math.floor(10.25))
print(math.ceil(10.25))
print(math.factorial(25))


print(help('modules'))

print(dir(math))
'''
'''
#open the file using the open() function
my_file_obj = open('myfile.txt','r') #always open to write or read
print('file pointer position',my_file_obj.tell())#tells you at which point the current cursor is.here it is ay beginning
print(my_file_obj.read())#reading the entire file
print('file pointer position',my_file_obj.tell())# now the cusrsor position is at the end
#close the file pointer obj and reset the file pointer position
my_file_obj.close() #closig the file

#open the file using the open() function
my_file_obj = open('myfile.txt','r')
#to read line by line
print(my_file_obj.read(15)) #read the first 15 characters

print(my_file_obj.readline()) #read line 1,that is it reads till the the new line character
print(my_file_obj.readline()) #read line 2
my_file_obj.close()

my_file_obj = open('myfile.txt','r')
#to read line by line using for loop
for each_line in my_file_obj: #can be used for searching and editing
   print(each_line)
my_file_obj.close()

my_file_obj = open('myfile.txt','r')
#to read all lines and return it back as a LIST
my_lines_list = my_file_obj.readlines()
print(my_lines_list)
my_file_obj.close()

#WRITING A FILE,Either we can append using 'a' or create a new file and write 
#using 'w' ( create a new file if the file does not exist)
my_file_obj = open('myfile.txt','a') # append always add the the content to the last of the file
my_file_obj.write("I shall give my parents,teachers and all elders")
my_file_obj.close()

#open the file using the open() function and read the contents
my_file_obj = open('myfile.txt','a')
my_file_obj.write("I shall give my parents,teachers and all elders")
my_file_obj.close()

#using 'w' (create a new file if the file does not exist)
my_file_obj = open('myfile.txt','w')
my_file_obj.write("I shall give my parents,teachers and all elders")
my_file_obj.close()

#X mode- if a file existis,it will remind if there is already a existing file
my_file_obj = open('mynew1file.txt','x')
my_file_obj.write(", firends and family")
my_file_obj.close()

my_file_obj = open('mynew1file.txt','r')
print('file pointer position',my_file_obj.tell())
print(my_file_obj.read())
print('file pointer position',my_file_obj.tell())
my_file_obj.close()


my_file_obj = open('mynew1file.txt','r')
my_file_obj.seek(16)
print(my_file_obj.read())
my_file_obj.close()

'''
'''
#DELETING A LINE FROM A FILE,NO BUILT IN FUNCTION

#opening the file read all line and save it as a list

file=open('fruits.txt','r')
lines=file.readlines()
file.close()
print(lines) #prints the lines in a list



todelete=input('\nEnter the fruit to delete:').strip()
file=open('fruits.txt','w')

for line in lines:
    if todelete in line:
        print(f'{todelete} is deleted')
    else:
        file.write(line)
file.close()

file=open('fruits.txt','r')

print(file.read())
'''
'''
import os


if os.path.exists('mynew1file.txt'):
    os.rename('mynew1file.txt','myrenamedfile.txt')
else:
    print('This file doesnt exists.')

'''

'''
import os

if os.path.exists('myrenamedfile.txt'):
    os.remove('myrenamedfile.txt')
    print('File removed')
else:
    print('This file doesnt exists.')
'''
'''
#ASSIGNMENT FILES

my_file = open('myfile.txt','r')
print(my_file.read())
my_file.close()

def listall():
    my_file=open('contacts.txt','r')
    lines=my_file.readlines()

    my_file.close()
    lines.sort()
    for name in lines:
        print(f'\n{name}')


   

def addnew(my_file):
    newname=input("\nEnter the name to add:")
    newnum=input('Enter the new number to add:')

    my_file=open('contacts.txt','r')
    my_file.read()
    my_file.close()

    my_file=open('contacts.txt','a')
    my_file.write('\n')
    my_file.write(newname)
    my_file.write(':')
    my_file.write(newnum)
    my_file.close()

    print('\nContact Added.')

def searchname():
    nametosearch=input('Enter the name to search:')

    my_file=open('contacts.txt','r')
    lines=my_file.readlines()
    my_file.close()

    for i in lines:
        if nametosearch in i:
            print(f'\n{i}\n')

def searchnum():
    numtosearch=input('Enter the name to search:')

    my_file=open('contacts.txt','r')
    lines=my_file.readlines()
    my_file.close()

    for i in lines:
        if numtosearch in i:
            print(f'\n{i}\n')

def deletename():  
    nametodelete=input('\nEnter the name to delete:').strip()

    my_file=open('contacts.txt','r')
    lines=my_file.readlines()
    my_file.close()    

    my_file=open('contacts.txt','w')
    for line in lines:
        if nametodelete in line:
            print(f'{nametodelete} is deleted')
        else:
            my_file.write(line)
    my_file.close()


print('\nPHONE DIRECTORY\n')

while True:
    print('\nMENU\n1.LIST ALL CONTACTS\n2.ADD NEW CONTACT\n3.SEARCH BY NAME\n4.SEARCH BY NUMBER\n5.DELETE BY NAME\n6.EXIT DIRECTORY')
    x=int(input('\nEnter the option:'))
    if(x==1):
        listall()
    if(x==2):
        addnew(my_file)
    if(x==3):
        searchname()
    if(x==4):
        searchnum()
    if(x==5):
        deletename()
    if(x==6):
        exit()


#INHERITANCE

'''

#PYHTON DECORATORS

#Decoartors are functions that can accept onaother function as argumnets ,then
#decorate it (add more functionalities) and then return ut back
#since we are not allowed to modify the passed function we used a wrapper function
#inside the function to add the additional functionality to the passed in function
#Then the wrapper function is returned


def my_decorator_fn(recieved_fn):
    def inner_wrapper_fn():
        print('Adding more functinality 1 to the recieved funtion')
        recieved_fn()
        print('Adding more functinality 2 to the recieved funtion')
    #returning functionality of recieved_fn()+ additional functionality 1 and 2
    return inner_wrapper_fn 


#defining a simple function
def function_to_decorate():
    print('Function having som ebasic functionality')
    print('that should not be changed')

#passing the function_to_decorate into the decorator
#it will return back the decoarted funtion 
my_decorated_fn=my_decorator_fn(function_to_decorate)
my_decorated_fn()

#using @ symbol we can specify the decorator at the time of fn definition itself
@my_decorator_fn
def function_to_decorate_new():
    print('Function having som ebasic functionality')
    print('that should not be changed')

function_to_decorate_new()











































