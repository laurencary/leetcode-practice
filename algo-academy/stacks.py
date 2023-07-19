# valid parenthesis

def isValid(s: str) -> bool:
    if len(s) % 2 == 1: return False 

    parens = {"(":")","{":"}", "[":"]"}
    stack = []
    for p in s:
        if p in parens:
            stack.append(p)
        elif parens[stack[-1]] == p:
            stack.pop()
        else:
            return False
        # print(stack)
    
    return True if len(stack) == 0 else False

# print(isValid("["))
# print(isValid("[]{}"))
# print(isValid("[]{(}"))

def 
