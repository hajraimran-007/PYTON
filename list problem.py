#Take a list of numbers from the user and find the smallest number.
numbers_list=[1,2,3,4,0,6]
print(min(numbers_list)) 

#Write a program to count how many times a given number appears in a list.
numbers_list=[1,2,3,2,4,2]
print(numbers_list.count(2))

#Create a list and separate even and odd numbers into two different lists.
numbers_list = [1, 2, 3, 4, 5, 6, 7]

even = []
odd = []

for n in numbers_list:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even:", even)
print("Odd:", odd)

#Write a program to find the second largest number in a list.
numbers_list=[1,2,5,7,9,10]
numbers_list.sort()
print("2nd largest num",numbers_list[-2])


