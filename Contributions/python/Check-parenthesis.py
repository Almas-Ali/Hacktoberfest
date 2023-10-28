'''
This program checks if the parenthesis are balanced or not.
It uses a stack to store the opening parenthesis and then
pops them out when a closing parenthesis is encountered.
If the stack is empty at the end, then the parenthesis are
balanced.
'''

def isValid(s: str) -> bool:
    stack = []
    p = {")":"(","]":"[","}":"{"}

    for char in s:
        if char in p:
            if stack and stack[-1] == p[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack


print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False