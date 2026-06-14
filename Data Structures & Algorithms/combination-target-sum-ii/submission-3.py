class Solution:
    def __init__(self):
        self.ans = []
        self.target = None

    def generateCombination(self, nums, stack = [], index = 0, curr_sum = 0):
        if curr_sum > self.target:
            return

        if curr_sum == self.target:
            self.ans.append(stack[:])

        prev = None
        for i in range(index, len(nums)):
            if prev == nums[i]:
                continue
            stack.append(nums[i])
            self.generateCombination(nums,stack,i+1, curr_sum+nums[i])
            stack.pop()
            prev = nums[i]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target= target
        candidates.sort()
        self.generateCombination(candidates)
        return self.ans