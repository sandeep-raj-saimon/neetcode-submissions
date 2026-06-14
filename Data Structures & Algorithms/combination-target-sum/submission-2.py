class Solution:
    def __init__(self):
        self.ans = []
        self.target = None
    
    def generateCombination(self, nums, start=0, stack=[], curr_sum=0):
        if curr_sum > self.target:
            return
        if curr_sum == self.target:
            self.ans.append(stack[:])
            return

        for i in range(start, len(nums)):
            stack.append(nums[i])
            self.generateCombination(nums, i, stack, curr_sum+nums[i])
            stack.pop()

        
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.generateCombination(nums)
        return self.ans