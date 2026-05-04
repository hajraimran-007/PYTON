#Given a list nums containing n distinct numbers in range [0, n], return the one missing number.
nums=[1,2,3,4]
n=4
for i in range(0,n+1):
    if i not in nums:
        print("missing num",i)
    else:
        print("not missing")    