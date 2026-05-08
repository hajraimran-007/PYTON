#Given a list of integers nums, return a new list where every element is squared
def list_num(nums):
    new_list = []

    for num in nums:
        new_list.append(num ** 2)

    return new_list


print(list_num([1, 2, 3, 4,5]))