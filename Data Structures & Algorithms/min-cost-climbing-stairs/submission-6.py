class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # if n <=2:
        #     return min(cost)

        # dp = [0 for _ in range(n+1)]
        # dp[0] = 0
        # dp[1] = 0
        # dp[2] = min(cost[:2])

        # for i in range(3,n+1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # return dp[-1]
        n = len(cost)

        dp = [-1 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        def recurse(idx):
            if idx < 0:
                return 0

            # if idx == 0:
            #     return cost[0]

            # if idx == 1:
            #     return cost[1]
            if dp[idx] != -1:
                return dp[idx]
            oneStep = cost[idx] + recurse(idx-1)
            twoStep = cost[idx] + recurse(idx-2)
            dp[idx] = min(oneStep, twoStep)
            return dp[idx]
        recurse(n-1)
        recurse(n-2)
        print(dp)
        return min(dp[-1], dp[-2])
        # return min(recurse(n-1), recurse(n-2))