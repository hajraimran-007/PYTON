#Given a string s containing only '(', ')', '{', '}', '[', ']', determine if the input string is valid. Open brackets must be closed in the correct order.
def isValid(s):
    list = []

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            list.append(ch)

        else:
            if not list:
                return False

            top = list.pop()

            if ch == ')' and top != '(':
                return False
            if ch == '}' and top != '{':
                return False
            if ch == ']' and top != '[':
                return False

    return len(list) == 0

print(isValid("()"))
print(isValid("([{}])"))
print(isValid("(]"))