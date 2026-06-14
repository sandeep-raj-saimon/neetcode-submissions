class Solution:
    def __init__(self):
        self.nums = None
        self.ans = []
    def generate(self, arr=[], m= {}):
        if len(arr) > len(self.nums):
            return
        if len(arr) == len(self.nums):
            self.ans.append(arr[:])
        
        for i in range(len(self.nums)):
            if m.get(self.nums[i]) is not True:
                arr.append(self.nums[i])
                m[self.nums[i]] = True
                self.generate(arr, m)
                arr.pop()
                m[self.nums[i]] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.generate()
        return self.ans