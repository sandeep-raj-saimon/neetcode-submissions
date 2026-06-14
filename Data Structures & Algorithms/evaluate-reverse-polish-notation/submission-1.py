class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '*', '-', '/']:
                if token == '+':
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    curr = ele1 + ele2
                elif token == '-':
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    curr = ele2 - ele1
                elif token == '*':
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    curr = ele1 * ele2
                else:
                    ele1 = stack.pop()
                    ele2 = stack.pop()
                    curr = int(ele2 / ele1)
                stack.append(curr)
            else:
                stack.append(int(token))
        return stack[-1]