class Solution:
    def __init__(self) -> None:
        self.ans = []
        self.nums = None
    def backTrack(self, index, stack):
        self.ans.append(stack[:])
        for i in range(index, len(self.nums)):
            stack.append(self.nums[i])
            self.backTrack(i+1, stack)
            stack.pop()
    def subsets(self, nums):
        self.nums = nums
        self.backTrack(0, [])
        return self.ans