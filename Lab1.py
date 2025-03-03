#programming syntax
print ("Hello World!")

#comments in python
x=1
#The initial value of x is 1
if x>0:
 print ("These two are comments") #Print a string

#take input from user
txt = input("Type something to test this out: ") 
print(txt)

#Multiple statements on a single line
print ("Statement1")
print ("Statement2")
#You can
print ("Statement1") ;print ("Statement2")

#indentation
x=1
if x>0:
 print("This statement has a single space indentation")
 print("This statement has a single space indentation")

x=1
if x>0:
    print("This statement has a single tab indentation")
    print("This statement has a single tab indentation")

x=1
if x>0:
    print("This statement has a single space+tab indentation")
    print("This statement has a single space+tab indentation")

#special characters in strings
print("This is a backslash (\\) mark.")
print("This is tab \t key.")
print("These are \'single qoutes\'")
print("These are \"double qoutes\"")
print("This is a new line\nNew Line.")

#string indices 
string1="Python Tutorial"
print(string1[0])  #print 1st character
print(string1[-15])  #print 1st character
print(string1[14])  #print last character
print(string1[-1])  #print last character
print(string1[4])  #print 4th character
print(string1[-11])  #print 4th character

#Lists
my_list1=[5,12,13,14]
print(my_list1)
my_list2=['red','blue','black','white']
print(my_list2)
my_list3=['red',12,112.12]
print(my_list3)

#List indices
color_list=["RED","BLUE","GREEN","BLACK"]
print(color_list[0]) 
print(color_list[0],color_list[3]) 
print(color_list[-1]) 

#List slices
print(color_list[0:2])
print(color_list[1:2]) 
print(color_list[1:-2])  
print(color_list[:3]) 
print(color_list[:]) 