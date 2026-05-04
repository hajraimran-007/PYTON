
'''Create a Python program that
Takes input of 5 numbers from the user
Stores them in a list (array)
Finds:
Total sum
Maximum number
Minimum number
'''
numbers_list =[]
for i in range(5):
    num=int(input("enter 5 nums"))
    numbers_list.append(num)
    print("numbers",numbers_list)
    total= sum(numbers_list)
    print(total)

print("Maximum:", max(numbers_list))
print("Minimum:", min(numbers_list))


