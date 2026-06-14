class Solution:
    def __init__(self):
        self.nums = None
        self.k = None
        self.ans = []
    def generate(self, arr = [], curr = 0, index = 0):
        """
        """
        if curr > self.k:
            return
        
        if curr == self.k:
            self.ans.append(arr[:])
        prev = None
        for i in range(index, len(self.nums)):
            if prev != self.nums[i]:
                arr.append(self.nums[i])
                prev = self.nums[i]
                self.generate(arr, curr+self.nums[i], i+1)
                arr.pop()
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        self.nums.sort()
        self.k = target
        self.generate()
        return self.ans