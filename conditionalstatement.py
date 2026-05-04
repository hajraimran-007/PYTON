#Stores your name, age, and city in variables
#Displays them in this format:
#My name is Ali, I am 20 years old, and I live in Lahore.
person = {
    "name":"HAJRA",
    "age":21,
    "city":"Rawalpindi"
}
print("My name is", person["name"] + ", I am", person["age"], "years old, and I live in", person["city"] + ".")

#Task 2: Simple Calculator
#Objective: Practice arithmetic operators.
n1 = int(input("enter number1="))
n2 = int(input("enter number2="))


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")
if choice == "1":
    print("Add",n1+n2)
elif choice=="2":
    print("Subtract",n1-n2)
elif choice=="3":
    print("Multiply",n1*n2)
elif choice=="4":
    print("divide",n1/n2)
else:
    print("invalid choice")    

#Task 3: Even or Odd Checker
n=int(input("enter number:"))

if n%2==0:
   print("even")
else:
    print("odd")

#Task 4: Student Marks and Grade
marks=int(input("enter marks:"))
if marks >=90:
    print("A")
elif marks >=80:
    print("B")
elif marks >=70:
    print("C")
elif marks >=60:
    print("D")
elif marks <=60:
    print("fail")

#Task 5: Multiplication Table:
n= int(input("enter number:"))
for i in range(1,11):
    print(i*n)

#Task 6: Sum of Numbers:
# Task 6: Sum of Numbers

total = 0

for i in range(1, 101):
    total = total + i

print("Sum of numbers from 1 to 100 is:", total)

#Task 7: List Operations
#Create a list of 5 fruits:
list=["apple","banana","grapes","orange","pear"]
print(list)
#Add one more fruit:
list.append("fig")
#Remove one fruit:
list.remove("banana")
#Display updated list
print(list)

#Task 8: Password Checker:
password =input("enter password:")
if password =="python123":
    print( "display “Access Granted")
else:
    print("Access Denied") 

#Task 9: Function for Square:
# Task 9: Function for Square

def square(num):
    return num * num

number = int(input("Enter a number: "))
print("Square =", square(number))

# Task 10: Mini Project – Attendance Checker

total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage =", percentage, "%")

if percentage >= 75:
    print("Allowed in Exam")
else:
    print("Not Allowed")

# Task 11: Guess the Number Game

secret_number = 7

guess = int(input("Guess the number: "))

if guess == secret_number:
    print("You Win!")
else:
    print("Try Again")    
    

<<<<<<<< HEAD:conditionalstatement.py
#Given {'a':10,'b':25,'c':15}, find the key with the maximum value.
dic={'a':10,'b':25,'c':15}
max_value=max(dic.values())
for key,value in dic.items():
    if value==max_value:
        print("Key with maximum value is:",key)
        break
#positive,negative or zero.poistive (is even or odd).
n=int(input("enter num :"))
if n>0:
    print("positive")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    if n==0:
        print("zero")
    else:
        print("negative")          

#Given a list of numbers, remove all duplicate values without using set().   
numbers_list=[1,2,3,4,2,5,1]
unique=[]
for i in numbers_list:
    if i not in unique:
      unique.append(i) 
    print(unique)     
========
>>>>>>>> e2112c937935957b41bd7735f2b3f32e6fb6c64f:problemsolving.py
