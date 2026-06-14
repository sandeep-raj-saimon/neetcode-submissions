class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <=2:
            return min(cost)

        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = min(cost[:2])

        for i in range(3,n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # print(dp)
        return dp[-1]