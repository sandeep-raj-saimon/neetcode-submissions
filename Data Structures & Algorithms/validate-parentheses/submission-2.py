class Solution:
    def isValid(self, s: str) -> bool:
        push_string = ["(", "{", "["]

        stack = []

        for string in s:
            if string in push_string:
                stack.append(string)
            else:
                if string == ")":
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if string == "}":
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                if string == "]":
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
                