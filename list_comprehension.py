#A list comprehension in Python is a short and clean way to create lists.
#stead of writing a full for loop, you can write everything in one line.

#1.create a square of list:
n=[1,2,3,4,5,6]
n= [i**2 for i in n]
print(n)

#2. Get even numbers only
even=[x for x in range(10) if x%2==0]
print(even)

#3.Convert names to uppercase
names=["sara","ali","ahmed"]
n=[name.upper() for name in names]
print(n)

#4.Create a list of lengths of words:
words=["hajra imran 007"]
n=[len(word)for word in words]
print(n)

#5.Using if-else inside list comprehension:
numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
