#Given a list of numbers nums, return a new list where each element is the cumulative sum up to that index:
def get_num(nums):
    total=0
    result=[]
    for i in nums:
        total=total+i
        result.append(total)
    return result
print(get_num([1,4,5,6,7]))      