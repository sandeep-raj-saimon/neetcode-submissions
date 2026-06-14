class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        lets start from back
        consider we reached the last index, we need to find whether we can reach starting point
        """

        n = len(nums)
        if n==1:
            return True
        curr = n-1
        i = n-2
        while (curr > 0 and i >= 0):
            if i + nums[i] >= curr:
                curr = i
            i-=1
            

        return curr <= 0