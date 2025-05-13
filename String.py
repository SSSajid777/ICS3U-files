"""
greeting= "Greetings to you" #Storing greeting in variable
name=input("Please enter your name:")
greeting=greeting+" "+ name
print(greeting)

"""


"""
message = "HELLO world"
print(message.capitalize())
print(message.upper())
print(message.lower())
print(message.title())
print(message.swapcase())

"""
"""
quote= "  To be, or not to be, that is the question… "
quote = quote.rstrip()
quote= quote+"."
print(quote)

lower_data= quote.lower()
print(lower_data)

"""
"""
message="Mr Ustrzycki's class is the worst class in the world."
message=message.replace("worst","best")
print(message)
print(message.find("best"))
print(message.rfind("best"))
message_list= message.split(" ")
print(message_list)
print(message_list[1]) 

"""

"""

quote = "Glory is fleeting, but obscurity is forever"

new_quote = quote.split(" ")

print(new_quote[2])

"""
"""
number=float(input("Enter a number:"))

if number%2==0:
    print("This number is even")
else:
    print("This number is odd") 

"""


"""


#input from user
title=input("Please enter your title:")


if title == "Excellency" or title == "Highness" or title=="Lord":
    print("Welcome your majesty")
else:
    print("Hi")


"""
"""
temp=input("Please enter the temperature")


c=temp

formula=c/5

formula1=f-32/9

formula1=formula

"""
"""

for i in range(1,12):
    print(2*i)
"""
"""
for i in range (10,-1,-1):
    print(i)
    import time
    time.sleep(1)
print ("Boom!")
"""
"""
rows=int(input("Enter the number of rows of stars:"))

for i in range(1,int(rows+1)):
    print ("*"*i)
  

  """
"""
    
for i in range(0,101,4):

   print(i)
    
"""
"""
#Ask user for their age
user_age=int(input("Please enter your age:"))

#Keep asking if that age is below 65
while user_age <65:
    user_age=int(input("Please enter your age:"))

"""
"""
print("Welcome to the game called Nim!")
print("Rules:")
print ("The game Nim starts out with seven sticks on the table.")
print("Each player takes turns picking up 1, 2 or 3 sticks and cannot pass.")
print("Whoever picks up the last stick loses (the other player wins).")   

sticks_num=7
#Ask if user wants to go first
input_player=input("Enter yes if you want to go first, enter no if u don't:")


if input_player=="no":
    print("Computer goes first and takes 2 sticks")
    sticks_num=sticks_num-2



while sticks_num >0:
    print ("There are",sticks_num,"sticks left. How many do you want to pick")
    input_2nd=int(input())
    if input_2nd==1 or input_2nd==2 or input_2nd==3:
        print("Error: Invalid pick. Please input again:")
        input_2nd=1
    

sticks_num=sticks_num - input_2nd

if sticks_num==0:
    print("You picked the last stick. Game Over!")

"""
"""
try:
    num1= int(input("Enter a number: "))
    num2= int(input("Enter another number: "))
    result= num1 / num2
    print("Result: ", result)
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
"""

try:
    value = int(input("Enter a number: "))
    result = 100 / value
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")




try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("That's not positive!")
except ValueError as e:
    print("Error: ", e)
else:
    print("Your number is ",number)
finally:
    print("Thank you for trying!")

"""
"""
    
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 122:
        raise ValueError("Age is too old!")
    print("Your age is", age)
except ValueError as e:
    print("Error:", e)
except:
    print("That's not a valid age!")
finally:
    print("That's for writing some code ICS3U1")

"""

#class_list=["Gin","Shin","Kag","Sad","Kon"]
"""

#index=int(input("Input your index number: "))

#for i in range(0,len(class_list

#print(class_list[index])

for name in class_list:
    print(name)
"""
    

#class_list.clear()
#print(class_list)
"""

list1 = [range(15,20,58,45,1,7)]
print(list1)
total = 0 
for number in list1:
    total += total + number
print(total)

"""
"""
nums = [1,2,3,4,5,6,7,8,9]
print(nums)

nums[3]=200

print(nums)


"""
"""
#2D lists
#COULD BE EXAM QUESTION
twoD = []   #Creates an empty list
twoD.append([])  #Adds an empty list at index 0
twoD.append([])   #Adds an empty list at index 1
twoD[0].append(1)
twoD[0].append(2)
twoD[1].append(3)
twoD[1].append(4)
print(twoD)
"""
"""
my_2d=[]
rows = int(input("Enter your number of rows:"))
columns = int(input("Enter your number of columns:"))
for i in range(0,rows):
 row = []
 print("Here's the next list of numbers:")
 for k in range(0,columns):
   val = int(input("Enter the next number:"))
   row.append(val)
 my_2d.append(row)
 #print(my_2d)

for i in my_2d:
  print(i)

"""
"""
#Create a user defined 2D list and 
print("Let's create a student list: ")
rows = int(input("How many students do you have: "))
columns = int(input("How many assignments do these students have: "))
students = []
titles = []
titles.append("Student Id")
for i in range(0,columns):
    assignment = input("Please enter name of assignment: ")
    titles.append(assignment)
"""
"""
#Dictionaries


temps={"January":[0,-7],"February":[0,-6],"March":[5,-2],"April":[12,3],"May":[20,11],"June":[24,15],"July":[28,18],"August":[26,18],"September":[22,14],"October":[15,8],"November":[8,2],"December":[3,-3]}

print(temps["March"])

for key in temps.keys():  #loop through keys
    print(key+":"+str(temps[key]))

for value in temps.values():  #loop through values
    print(value)

for key, value in temps.items():  #loop both keys and values
    print(key+":"+str(value))


marks={} #empty dictionary

marks["Test1"]=90   #Add the first mark

marks.update(Test2 = 85)   # Add the 2nd mark using update

marks_set = {"Test3":25,"Test4":72,"Test5":66} #Create a dictionary
marks.update(marks_set) #update the whole dictionary to marks

print(marks)  #prints 5 mark dictionary


#Option 1 by keys
for key in marks.keys():
    print(key+":"+str(marks[key]))

#Option 2 by value
for value in marks.values():
    print(value)

#Option 3 by item
for key, value in marks.items():
    print(key+":"+str(value))

#Sorting the dictionary
for item in sorted(marks):
    print(item+":"+str(marks[item]))

#Reverse Order

for item in sorted(marks, reverse=True):
    print(item+":"+str(marks[item]))

"""
"""
from random import randint

#Write a Python script to sort (ascending and descending) a dictionary by value (populate dictionary using random numbers).
rand_dict = {}

for i in range(0,20):

    rand_dict[i] = randint(0,1000)
print(rand_dict)

vals = list(rand_dict.values())
vals.sort()
count = 0
for val in vals:
    rand_dict[count] = val
    count+=1
print(rand_dict)



my_dict = {}
key = input("Please enter a key: ")
val = input("Please enter a value: ")
my_dict[key] = val
print(my_dict)



#Create a user defined 2D list and 
print("Let's create a student list: ")
rows = int(input("How many students do you have: "))
columns = int(input("How many assignments do these students have: "))
students = []
titles = []
titles.append("Student Id")
for i in range(0,columns):
    assignment = input("Please enter name of assignment: ")
    titles.append(assignment)

students.append(titles)
for i in range(0,rows):
    student = []
    for k in range(len(titles)):
        value = int(input("Please enter value for column "+str(titles[k])+" "))
        student.append(value)
    students.append(student)
    print(students)


"""

#Functions
"""
def is_prime(user_num):
 for i in range(2,user_num//2+1):
   if user_num%i ==0:
     return False
 return True


ex = False

while not ex:
 prime_check = int(input("Please enter a number that you think is prime (enter -1 to exit): "))
 if prime_check==-1:
   ex = True
 else:
   print(str(prime_check)+" Is this a prime? "+str(is_prime(prime_check)))
"""
"""
#function that will take in 3 numbers and RETURN the largest number (possible exam question)


def largest_three(num1,num2,num3):
 if num1>=num2 and num1>=num3:
   return num1
 elif num2>=num1 and num2>=num3:
   return num2
 return num3

user_num1 = int(input("Please enter 1st number: "))
user_num2 = int(input("PLease enter 2nd number: "))
user_num3 = int(input("Please enter 3rd number: "))
largest = largest_three(user_num1,user_num2,user_num3)

print(largest)

"""


#classes and objects


