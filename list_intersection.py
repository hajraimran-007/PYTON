#Given two lists a and b, return a list of elements that appear in both (without duplicates)
def list_num(a, b):
    common=list(set(a)&set(b))
    return common

print(list_num([1,2,3],[2,3,4]))