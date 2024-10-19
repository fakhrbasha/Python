import random
from typing import Self
import Module

# comment 
# to print : 
print ("Hello World")

'''
comment
'''
#variable
x=5
y=6
print(x+y)
z = "hello sir"
print (z)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#Get the Type 
print(type(x)) #str
print(type(y)) #int


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a Collection
friut=["apple" , "Banana"]

x,y=friut
print (x)
print (y)
x = 5
y = "John"
print(x, y)
"""x = 5
y = "John"
print(x+ y) #error"""

#Global Variables

x="Ahmed"

def myfunc():
    print ("Py " + x)

myfunc()
#global Keyword
def Myfunc():
    global x 
    x="Ahmed"
    print ("My name is " + x)

print ("I am "  + x)

#Data Types
'''
Text Type:	                str
Numeric Types:	            int, float, complex
Sequence Types:              list, tuple, range
Mapping Type:	            dict
Set Types:	                set, frozenset
Boolean Type:	            bool
Binary Types:	            bytes, bytearray, memoryview
None Type:	                 NoneType

'''

x = 5
print(type(x)) #<class 'int'>

#Numbers
x = 1 
y = 1.5
z = 1j
print(type(x))
print(type(y))
print(type(z))

x= 10
a=float(x)
print(a)
y=20.2
b=complex(y)
print(b)
#Random Number
#Import the random module, and display a random number between 1 and 9:
print (random.randrange(1,10 ))
#String
x="hello World"
print(x[0])
for x in "Banana":
    print(x)

# String Length
x="ahmed"
print(len(x))
# Check String
txt= "ahmed Mohamed salah"
print("Moha" in txt) #true

if "Mo" in txt:
    print("Yes")

print("Mo" not in txt) 

#Slicing
a="Hello World"
print(a[2:5]) # idx 2 3 4 llo
print(a[:5]) # 0 1 2 3 4 
print(a[2:]) # 2 -> final

#Modify Strings
a="aLi"
print(a.upper())
print(a.lower())
#The strip() method removes any whitespace from the beginning or the end:
a="   ahmed Mo    "
print(a.strip())

#The replace() method replaces a string with another string:
a="Ahmed Mohamed"
print(a.replace("A" , "M"))
#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Concatenation
a="ahmed"
b=" fakhr"
print(a+" "+b)


#Format - Strings

age = 22
txt = f"My age is {age}"
print (txt)

#bool
print(10>5)

#List 
mylist=["ahmed" , "Mohamed ", "salah"] 
print(mylist)
for x in mylist:
    print(x)

print(len(mylist))
print(mylist[0])
list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(mylist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # 2 3 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # 0 1 2 3

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1]="ahmed"
print(thislist)

# Add List Items
list=["ahmed" , "Mohamed" , "salah"]
list.append("fakhr")
print(list)
#Insert Items
list.insert(1 , "Basha")
print(list)

#Extend List
#To append elements from another list to the current list, use the extend() method.
list1=["ahmed","ali" , "Mo"]
list2=["Samy" , "Salary"]
list1.extend(list2)
print(list1)

# Remove List Items
list=["ahmed" , "ali" , "Salah"]
list.remove("ali")
list.pop(1)
print(list)

#Loop Lists
list = ["ahmed" , "Mohamed" , "Salah"]
for x in list:
    print(x)
for x in range(len(list)): #print index Number
    print(x)

#While Loop
list = ["ahmed" , "Mohamed" , "Salah"]
i = 0
while i < len(list):
    print(list[i])
    i = i+1

# Comprehension
list = ["ahmed" , "mohamed" , "salah","sory"]
newlist=[]
for x in list:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Reverse Order
thislist.reverse()
print(thislist)

# Copy Lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Tuples
mytuple=("ahmed" , "Mohamed" ,"Salah")
print(mytuple)
print(len(mytuple))
print(mytuple[0])
print(mytuple[-1]) # salah
#append
#remove
#same list


#set
myset = {"ahmed" , 1,2,3}
print(myset)
print(len(myset))
# same list 



# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
mydic = {
    "brand" : "BMW",
    "Model"  : "2001",
    "Color" : ["red","Blue"]
}
print(mydic) #{'brand': 'BMW', 'Model': '2001', 'Color': ['red', 'Blue']}
print(mydic["brand"]) #BMW
print(len(mydic))

dic = dict(name = "BMX" , Model = "C200" , Year="2000")
print(dic) #{'name': 'BMX', 'Model': 'C200', 'Year': '2000'}
x=dic.get("name")
print(x)
x=dic.keys()
print(x) #dict_keys(['name', 'Model', 'Year'])
x=dic.values()
print(x) #dict_values(['BMX', 'C200', '2000'])
x = dic.items()
print(x) #dict_items([('name', 'BMX'), ('Model', 'C200'), ('Year', '2000')])
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# if
# else if = elif
x = 20
y = 30
if x > y :
    print ("Hi")
elif x==y:
    print("No")
else :
    print("Bye")


a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# Loops
i= 1 
while i < 5:
    print (i)
    i+=1

# break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



# for loop
x = ["Apple" , "Banana" , "Orange"]
for i in x:
  print(i)

for x in "Apple":
  print(x)

# range() Function
for x in range(6):
  print(x)

# range 2 - 6
for x in range(2,6):
  print(x)

# inc
for i in range( 2,10,3): # print 2 -> 10  i+=3
  print(i)

# function
def myfun():
  print("Hi")

myfun()

def myfu():
  for i in range(5):
    print(i)

myfu()

# Arguments
def Name(fname):
  print(fname + " HI")

Name("Ahmed")

# prametar or Argument
def my_f(lname,fname):
  print(fname + " " + lname)

my_f("Ahmed" , "Ali")

# Arbitrary Arguments, *args

def fun(c1,c2,c3):
  print("Hi MR " + c2)


fun(c1="A" , c2="B"  , c3="X")

# Arbitrary Keyword Arguments, **kwargs
def f(**k):
  print("Hi Mr " + k["Lname"])

f(fname="Ali" , Lname="MO")

# Default Parameter Value

def mydef(country="Egypt"):
  print("UR Country is " + country)

mydef("Swddf")
mydef()

# Passing a List as an Argument
def mylit(food):
  for x in food:
    print (x)

x= ["Apple" , "Banana" , "Orange"]
mylit(x)

# Return Values
def r(x):
  return 5 * x

print(r(5)) # 25

# Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    #6 5 4 3 2 1
    # 1 
    # 1 + 2  = 3
    # 1 + 2  + 3 = 6
    # 1 + 2  + 3 + 4= 10 etc
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Lambda : anonymous function
'''
Syntax
lambda arguments : expression

'''
# Add 10 to argument a, and return the result:
x = lambda a : a+10
print(x(5))

x = lambda a,b : a*b 
print(x(4,5))
x = lambda a,b,c : a+b+c
print(x(5,5,5))

# Use Lambda Functions

def myfunc(n):
  return lambda a : a*n

m = myfunc(2)
print(m(2))



# Arrays

# Adding Array Elements append 
# Removing Array Elements pop(idx) || remove (value)
''' 
Method	Description
append()	Adds an element at the end of the list
clear()	  Removes all the elements from the list
copy()	  Returns a copy of the list
count()	  Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	  Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	  Sorts the list

'''

# Classes/Objects
# Create a class named MyClass, with a property named x:
class myclass:
  x=5
  y=3
# create object
p1 = myclass()
print(p1.x)
print(p1.y)

# The __init__() Function
class preson:
  def __init__(self,name,lname):
     self.name = name
     self.lname = lname


p1 = preson("Join" , "Fakhr")
print(p1.name)
print(p1.lname)

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class person:
  def __init__(self , age , porn):
     self.age = age
     self.porn = porn + 20

p = person(22 , 23 )
print(p.age)
print(p.porn)

# The __str__() Function
class preson:
  def __init__(self,name,lname):
     self.name = name
     self.lname = lname
  def __str__(self):
     return f"{self.name}({self.lname} )"

p = preson("Ali" ," Mo") #object

print(p)

class person:
  def __init__(self , name ,age):
      self.name=name
      self.age = age
  def fun(self):
     print(" HI Mr : " + self.name)
#create object

p = person("ahmed" , 20)
# call fun 
p.fun()

class age:
  def __init__(Fakhr,age):
    Fakhr.age=age
  def math(Fakhr):
    Fakhr.age = age 
  def p(Fakhr):
     print(abs(Fakhr.age - 2024))

p = age(2004)
p.age=2003 #Modify Object Properties
c = age(2000)
c.age = 2000
del c # delete object
p.p()




# Inheritance
# create parent class
class Person:
  def __init__(self , name , age):
    self.name = name
    self.age = age
  def p(self):
    print("Ur Namr Is : " + self.name + " UR AGE : " , self.age)
    


# create object
name1 = Person("Fakhr" , 20)
name1.p()

# create child class
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  def __init__(self, name, age , year):
     super().__init__(name, age) # inhirt all method and properties
     self.grad=year
     # add method
  def Welcome(self):
     print("Name : " + self.name + " Age : " , self.age , " Grad : " , self.grad )


e = Student("Mousa" , 30 , 2020)
e.Welcome()

# Iterators
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class it:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x=self.a
    self.a+=1
    return x 

my = it()
myiter =iter(my)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class itere:
  def __iter__(self):
    self.a=1
    return self
  def __next__(self):
    if self.a <= 20:
      x=self.a
      self.a+=1
      return x
    else:
      raise StopIteration
  
myit=itere()
miter = iter(myit)
for  i in miter:
  print(i)

# Polymorphism
"""
class car1:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  def move(self):
    print("BMW")


class car2:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  def move(self):
    print("Hondai")


class car3:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("Fiat")

x=car1("BMW" , "2004")
y=car2("Hondai"  , "2011")
z=car3("Fiat ", "2000")
for i in (car1,car2,car3):
  i.move()"""

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

class Car:
  def __init__(self,name,model):
    self.name=name
    self.model=model
  def move(self):
    print("divv")

class Var(Car):
  pass

class dev(Car):
  def move(self):
    print("dev")

class div(Car):
  def move(self):
    print("div")

car1 = Var("BMW" , "2022")
car2=dev("Hondia" , "2112")
car3=div("Fiat" , "2021")

for x in (car1,car2,car3):
  print(x.name)
  print(x.model)
  x.move()

# Modules
# Create a Module
#To create a module just save the code you want in a file with the file extension .py:
# import module 
# Note: When using a function from a module, use the syntax: module_name.function_name.
Module.name("Fakhr")
print(Module.person)

# Naming a Module
# Re-naming a Module Use import old_name as new_name

import Module as MD
x = MD.person["name"]
print(x)
import platform
x = dir(platform) # machine info 
print(x)

# What is the correct syntax of printing all variables and function names of the "mymodule" module?
x = dir(MD)
print(x)

#  Dates
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.day)
print(x.strftime("%A")) # day
# Creating Date Objects
                   #Year-month-day
x = datetime.datetime(2004,5,17)
print (x)

# Built-in Math Functions
x=max(7,8,9)
y=min(7,8,9)
print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3) # 4*4*4

print(x)
# import math
import math
x= math.ceil(4.7)
print(x)
import Module as mx
x = mx.mx(7,8)

# User Input

user=input("Enter UR Name : ")
print("UR Name is : " + user)


# -------- End PYTHON  See You Later --------- #

