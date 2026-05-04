#A list in Python is a collection (data structure) used to store multiple values in a single variable.
numbers_list = [1,2,3,4,5]
print(numbers_list)
print("print after changing the list")
numbers_list[1]= 7
print(numbers_list)
numbers_list.append(9) # add one item at the end
print(numbers_list)
numbers_list.extend([6,10]) # extend mean adding two values seprately
print(numbers_list)
numbers_list.insert(2,12) #insert matlab add karna specific position ma
print(numbers_list)
numbers_list.pop() #remove last element specfic index value likh ka bhi remove kar sakte
print(numbers_list)
numbers_list.remove(7) #remove any num from list
print(numbers_list)
numbers_list.clear() #clear full list
print(numbers_list)
