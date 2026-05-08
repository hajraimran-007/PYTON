#Given a tuple t and an index i, return the element at index i. If i is out of range, return -
def tuple_num(t, i):
    if i >= 0 and i < len(t):
        return t[i]
    else:
        return -1


print(tuple_num((10, 20, 30), 1))
print(tuple_num((10, 20, 30), 2))
        
