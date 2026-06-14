class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None

    def generate(self, index = 0, stack = []):
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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.nums.sort()
        self.generate()
        return self.ans
        