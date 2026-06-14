class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [-1 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        def recurse(n):
            if n <= 1:
                return 1
            if dp[n] != -1:
                return dp[n]
            dp[n] = recurse(n-1) + recurse(n-2)
            return dp[n]


        recurse(n)

        return dp[-1]