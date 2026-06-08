#Given a list nums and integer k, rotate the list to the right by k positions.
def list_num(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
print(list_num([1,2,3,4,5,6], 2))
    
    