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
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2,n):
            current = dp[i-2] + nums[i]
            skip = dp[i-1]
            dp[i] = max(current, skip)
        # def recursion(index, curr_sum = 0):
        #     if index == 0:
        #         return nums[0]

        #     if index == 1:
        #         return max(nums[:2])

        #     if dp[index] != 0:
        #         return dp[index]

        #     current = recursion(index-2) + curr_sum + nums[index]
        #     skip = recursion(index-1) + curr_sum
        #     dp[index] = max(current, skip)
        #     return max(current, skip)

        # recursion(n-1)
        return dp[-1]
