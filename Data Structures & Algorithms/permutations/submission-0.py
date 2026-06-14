class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None
    def generate(self,stack = [], m = None):
        print(m, stack)
        if m is None:
            m = {}
        if len(stack) == len(self.nums):
            self.ans.append(stack[:])
            return
        for i in range(len(self.nums)):
            if m.get(i) is True:
                pass
            else:
                stack.append(self.nums[i])
                m[i] = True
                self.generate(stack, m.copy())
                stack.pop()
                m[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.generate()
        # for i in range(len(nums)):
        #     self.generate(i)
        return self.ans