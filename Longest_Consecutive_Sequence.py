#Given a list of integers nums, return the length of the longest consecutive elements sequence. 
def longestConsecutive(nums):
    if not nums:
        return 0

    nums=sorted(set(nums))

    longest = 1
    current = 1

    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1] - 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1

    longest = max(longest, current)
    return longest


nums = [0,3,19,2,5,10,1,7,0,0]
print(longestConsecutive(nums))