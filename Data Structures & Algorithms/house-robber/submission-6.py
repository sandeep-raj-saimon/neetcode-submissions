class Solution:
    def __init__(self):
        self.ans = 0
    def rob(self, nums: List[int]) -> int:
        """
        find max of all possible ways
        """
        
        n = len(nums)
        if n <=2:
            return max(nums)

        prev2 = nums[0]
        prev = max(nums[:2])
        for i in range(2,n):
            current = prev2 + nums[i]
            skip = prev
            prev2 = prev 
            prev = max(current, skip)
        return prev
