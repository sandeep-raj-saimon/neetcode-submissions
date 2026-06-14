class Solution:
    def __init__(self):
        self.nums = None
        self.k = None
        self.ans = []

    def generate(self, arr=[], curr=0, index=0):
        if curr == self.k:
            self.ans.append(arr[:])
        if curr > self.k:
            return

        for i in range(index, len(self.nums)):
            arr.append(self.nums[i])
            self.generate(arr, curr+self.nums[i], i)
            arr.pop()
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.k = target
        self.generate()
        return self.ans