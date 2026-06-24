class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = float('inf')

        while self.stack:
            mini = min(mini, self.top())
            tmp.append(self.pop())

        while tmp:
            self.stack.append(tmp.pop())

        return mini