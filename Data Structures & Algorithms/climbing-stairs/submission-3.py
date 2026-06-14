class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n==1:
            return n
        dp = [0 for _ in range(n+1)]

        dp[0]=1
        dp[1] = 1

        prev = dp[1]
        prev2 = dp[0]

        for i in range(2, n+1):
            dp[i] = prev + prev2
            prev2 = prev
            prev = dp[i]

        return prev