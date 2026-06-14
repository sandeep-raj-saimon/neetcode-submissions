class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None
        self.target = None

    def generate(self, index = 0, stack = []):
        if sum(stack) > self.target:
            return
        if sum(stack) == self.target:
            self.ans.append(stack[:])
        if index >= len(self.nums):
            return
        
        prev = None
        for i in range(index, len(self.nums)):
            if prev == self.nums[i]:
                pass
            else:
                stack.append(self.nums[i])
                self.generate(i+1, stack)
                stack.pop()
            prev = self.nums[i]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        self.target = target
        self.nums.sort()
        self.generate()
        return self.ans
        