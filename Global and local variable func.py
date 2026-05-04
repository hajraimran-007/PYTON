#A global variable declared outside any function. It can be accessed anywhere in the program.
y="im global"#global variable
def show():
    print(y)#accessed inside the func
show()
print(y) #also accessed outside
#A local variable declared inside a function. It can only be used within that function.
def show():
    y = 50  # Local variable
    print(y)  #Works fine here

show()       # Output: 50
print(y)     # ERROR: y is not defined

#example:
x = "I am GLOBAL"       #Global variable

def my_function():
    y = "I am LOCAL"    # Local variable
    print(x)            # Can access global
    print(y)            # Can access local

my_function()
print(x)                # Works
print(y)                # Error — y doesn't exist here
