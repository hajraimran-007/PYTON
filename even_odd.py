def get_num(nums):
    result=[]
    for i in nums:
        if i%2==0:
           result.append("even")
        else:
            result.append("odd")
    return result
print(get_num([1,2,3,4,5,6,7]))              
