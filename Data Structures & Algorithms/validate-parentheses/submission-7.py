class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(', '{', '[']
        close = [')', '}', ']']
        for e in s:
            if e in opens:
                stack.append(e)
            else:
                if len(stack) > 0:
                    p = stack[-1]
                    if (e == ')' and p == '(') or (e == '}' and p == '{') or (e == ']' and p == '['):
                        stack.pop()
                    else:
        
                        return False
                else:
                    return False
        
        return True if len(stack) == 0 else False
