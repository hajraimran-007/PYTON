#A function is a reusable block of code that performs a specific task. Instead of writing the same code repeatedly, you define it once and call it whenever needed.
#Defining a Function
def function_name(parameters):
    """Docstring (optional): describes what the function does"""
    # code block
    return 
#def — keyword to define a function
#function_name — name you give the function
#parameters — inputs (optional)
#return — sends back a result (optional)...

#Types of Functions:
#1. No parameters, no return value
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!

#2.With parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")  # Output: Hello, Ali!

#3.With return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

#quick summary
'''def  →  define a function
()   →  parameters go here
:    →  start the code block
return → send back a result'''





