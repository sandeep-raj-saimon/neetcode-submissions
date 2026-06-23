class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0

        for token in tokens:
            ans = None
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                ans = (a+b)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                ans = (b-a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                ans = (a*b)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                ans = int(b/a)
            else:
                stack.append(int(token))

            if ans is not None:
                stack.append(ans)

        return stack[-1]