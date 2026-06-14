class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None
        self.target = None
    def backTrack(self, index, stack):
        
        if sum(stack) == self.target:
            self.ans.append(stack[:])
            return
        elif sum(stack) > self.target:
            return
        
        for i in range(index, len(self.nums)):
            stack.append(self.nums[i])
            self.backTrack(i, stack)
            stack.pop()

    def combinationSum(self, nums, target: int):
        self.nums = nums
        self.target = target
        self.backTrack(0, [])
        return self.ans