class Solution:
    """
    min ans is 1
    start from backwards
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        n = len(nums)
        ans = 1
        dp = [1 for _ in range(len(nums))]

        for i in range(n-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(dp[i], ans)
        return ans