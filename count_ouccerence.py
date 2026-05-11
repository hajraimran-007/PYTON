#Given a list nums and a value target, return how many times target appears in nums without using list.count():
def count_num(nums,target):
    count=0
    for i in nums:
        if i==target:
            count+=1 
    return count
print(count_num([1,2,3,2,5,6,2],2))           
