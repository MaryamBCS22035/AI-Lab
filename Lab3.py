#Q1: print numbers between 1500 and 2700 which are divisible by 7 and multiple of 5
for i in range(1500,2701):
 if i%7==0 and i%5==0:
  print(i)

#Q2: temperature conversion
celsius= float(input("Enter temperature in celsius "))
fahrenheit= (celsius * 1.8) + 32
print("Temperature in fahrenheit is ",fahrenheit)

fahrenheit = float(input("Enter temperature in fahrenheit "))
celsius= (fahrenheit-32)/1.8
print("Temperature in celsius is ",celsius)

#Q3: guess a number
import random
number = random.randint(1, 9)
guess=int(input("guess a nummber between 0 and 9 "))
while(guess!=number):
 print("Your guess was wrong")
 guess=int(input("Guess again "))
print("Well guessed")

#Q4: print a pattern
for i in range(1,6):
 for j in range(1,i+1):
  print("*",end="")
 print()
for i in range(1,5):
 for j in range(i,5):
   print("*",end="")
 print()

#Q5: reverse a word
word= input("Enter a word ")
reverse = word[::-1]
print(reverse)

#Q6:count even and odd numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even= 0
odd= 0
for num in numbers:
    if num % 2 == 0:
        even+=1
    else:
        odd+= 1
print("Number of even numbers:", even)
print("Number of odd numbers:", odd)

#Q7:item and their datatype
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for i in datalist:
    print("Item: ",i,end=" ")
    print("Type: ",type(i))

#Q8:print numbers expect 3 and 6
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)

#Q9: fibonacci
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b


for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Q10:two dimensional array
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
array = [] 
for i in range(m):
    row = []  
    for j in range(n):
        row.append(i * j)  
    array.append(row) 
for row in array:
    print(row)

#Q11:lower case letters
lines = []

print("Enter lines of text (press Enter on a blank line to stop):")
while True:
    line = input()
    if line == "": 
        break
    lines.append(line.lower())  

for line in lines:
    print(line)

#Q12: comma separated sequence
binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')
divisible_by_5 = []
for num in binary_numbers:
    if int(num, 2) % 5 == 0:
        divisible_by_5.append(num)

print(",".join(divisible_by_5))


#Q13: number of digits and letters
str = input("Enter a string: ")
letter = 0
digit= 0

for i in str:
    if i.isalpha(): 
        letter += 1
    elif i.isdigit():  
        digit += 1
print("Number of letters:", letter)
print("Number of digits:", digit)

#Q14: password validation
import re
password = input("Enter password: ")
if (6 <= len(password) <= 16 and
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"[0-9]", password) and
    re.search(r"[$#@]", password)):
    print("Valid Password")
else:
    print("Invalid Password")
