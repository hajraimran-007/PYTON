#Given a tuple t of exactly two elements, return a new tuple with the elements swapped.
t=(1,2)
tn=list(t)
tn[0],tn[1] = tn[1],tn[0]
t=tuple(tn)
print(tn)