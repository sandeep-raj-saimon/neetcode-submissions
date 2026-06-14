class MinStack:

    def __init__(self):
        self.stack = []
        self.track = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = []
        while len(self.track) != 0 and self.track[-1] < val:
            last = self.track[-1]
            self.track.pop()
            temp.append(last)
        self.track.append(val)
        for ele in reversed(temp):
            self.track.append(ele)

    def pop(self) -> None:
        last_element = self.stack[-1]
        print(self.track)
        # last_element has to be removed from both stacks
        temp = []
        while len(self.track) != 0:
            ele = self.track[-1]
            if ele == last_element:
                self.track.pop()
                break
            else:
                temp.append(ele)
                self.track.pop()
        print(temp)
        for ele in reversed(temp):
            self.track.append(ele)
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.track[-1]
