# Given a list of integers nums and an integer target, return indices of the two numbers that add up to target.
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

num = [2, 3, 4, 5, 6, 7]
target = 9

result = two_sum(num, target)
print(result)

