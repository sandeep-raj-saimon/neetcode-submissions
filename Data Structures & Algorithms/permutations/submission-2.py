class Solution:
    def __init__(self):
        self.ans = []
        self.len = None
    def generatePermutation(self,nums, stack=[], freq = {}):
        if len(stack) == self.len:
            self.ans.append(stack[:])
            return

        for i in range(len(nums)):
            if freq.get(nums[i]) is None:
                freq[nums[i]] = 1
                stack.append(nums[i])
                self.generatePermutation(nums, stack)
                stack.pop()
                del freq[nums[i]]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.len = len(nums)
        self.generatePermutation(nums)
        return self.ans
        