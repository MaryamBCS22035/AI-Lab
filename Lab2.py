#while loop
count = 0
while (count < 10):
  count = count + 1 
  print("Hello World")

#for loop
print("List Iteration")
list = ["Maryam", "Muneeba", "Aqsa","Fatima"] 
for i in list:
  print(i)

print("\nTuple Iteration")
tuple = ("Zartasha", "Isba", "Ifra") 
for i in tuple:
  print(i)

print("\nString Iteration") 
str = "Hello"
for i in str:
  print(i)

list1 = ["Nida", "Umaira", "Dua"] 
for index in range(len(list1)):
  print(list1[index])

# Prints all letters except 'e' and 's'
for letter in 'bscssemster6':
  if letter == 'e' or letter == 's': continue
  print ('Current Letter :', letter) 
  
# break the loop as soon it sees 'e' or 's'
for letter in 'hello':
  if letter == 'e' or letter == 's': break
  print ('Current Letter :', letter)

#creating a functiom
def my_function(): 
  print("Hello from a function")
my_function()

#Parameters
def my_function(degree):
 print(degree + " 6th Semester")
my_function("BSCS")
my_function("BSIT")

#Default Parameter Value
def my_function(country ="Pakistan"): print("I am from " + country)
my_function()
my_function("UK")

#List as parameter
def my_function(food):
 for x in food: print(x)
fruits = ["apple", "banana", "cherry"] 
my_function(fruits)

#return values
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#class
class MyClass: x = 5

#object
p1 = MyClass() 
print(p1.x)

#init funtion
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
   print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)
p1.myfunc()