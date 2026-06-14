class Solution:
    def __init__(self):
        self.ans = []
        self.len = None
    def generateSubsets(self, nums, index = 0, stack = [],prev = None):
        if index > self.len:
            return

        self.ans.append(stack[:])
        for i in range(index, len(nums)):
            if prev == nums[i]:
                continue
            stack.append(nums[i])
            self.generateSubsets(nums, i+1, stack)
            stack.pop()
            prev = nums[i]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.len = len(nums)
        self.generateSubsets(nums)
        return self.ans
        