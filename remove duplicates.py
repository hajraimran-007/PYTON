#Given a list nums, return a new list with duplicates removed while preserving the original order.
nums=[4,2,6,4,1,5,2,3]
result=[]
for i in nums:
    if i not in result:
        result.append(i)
print(result)        
