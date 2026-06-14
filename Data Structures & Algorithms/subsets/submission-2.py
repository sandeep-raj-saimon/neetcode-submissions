class Solution:
    def __init__(self):
        self.ans = []
        self.nums = None

    def recursion(self,index=0, arr=[]):
        self.ans.append(arr[:])
        if index >= len(self.nums):
            return
        for i in range(index, len(self.nums)):
            arr.append(self.nums[i])
            self.recursion(i+1, arr)
            arr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.recursion()
        return self.ans