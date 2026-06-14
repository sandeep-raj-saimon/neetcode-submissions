class Solution:
    def __init__(self):
        self.ans = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        def recurse(index=0, stack=[]):
            self.ans.append(stack[:])
            if index >= n:
                return
            prev = None
            for i in range(index,n):
                if nums[i] == prev:
                    continue
                stack.append(nums[i])
                recurse(i+1, stack)
                stack.pop()
                prev = nums[i]
            
        recurse()
        return self.ans