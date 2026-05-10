#Given two lists keys and values of the same length, return a dictionary mapping each key to its
#corresponding value.
def list_num(key,value):
    result=dict(zip(key,value))
    return result
print(list_num(key=["hajra","maira"],value=[21,22]))