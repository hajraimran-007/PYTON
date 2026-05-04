#Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print("number from 1 to 10", i)

#Print all even numbers from 1 to 20.
for even in range(2,21,2):
    print("even numbers are:", even)

#Take a number from user and print its multiplication table (e.g., 5 → 5×1=5 … 5×10=50). 
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

 #Calculate the sum of numbers from 1 to n (user input).
n = int(input("Enter number for sum: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum is:", total)      
         
 #Print numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
       print(i)
   
#Count how many even and odd numbers are in a list.
numbers=[1,2,3,4,5,6,7,8,9]
even=0
odd=0

for n in numbers:
    if n % 2 == 0:
       even+=1
    else:
        odd+=1

print("even",even)
print("odd",odd)

  # Find the factorial of a number using a loop.
n=int(input("enter numbers"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#using while loop
n=int(input("enter numbers"))
fact= 1
i= 1
while i<=n:
    fact= fact*i
    i=i+1
    print(fact) 
#print all numbers between 1 to 100 that are divisible by 3 and 5.
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print(n)

#print * in square form:
for row in range(5):
    for col in range(4):
        print("*",end=" ")
    print()

# Print different pattern:   
for row in range(5):
   for col in range(row+1):
       print("*", end=" ")
   print() 
#everse a number (e.g., 123 → 321).
n=int(input("enter num"))
rev=0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("reversed",rev)

# counting digit
n=int(input("enter the num:"))
counter=0
while n>0:
    counter+=1
    n=n//10
    print("total digit",counter)
    # simple2
n = input("Enter number: ")
print("Total digits:", len(n))

#sum all the even number given by user using while loop
n = int(input("How many numbers: "))
i=0

even_sum = 0

while i <= n:
    num = int(input("Enter number: "))
    
    if num % 2 == 0:
        even_sum += num
    
    i += 1

print("Sum of even numbers:", even_sum)

   
