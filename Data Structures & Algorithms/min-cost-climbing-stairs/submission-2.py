class Solution:
    def __init__(self):
        self.cost = None
    
    # recurcion code
    def minCost(self, n):
        if (n < 0):
            return
        
        if (n < len(self.cost) - 2):
            current_cost = self.cost[n] + min(self.cost[n+1], self.cost[n+2])
            self.cost[n] = current_cost
            self.minCost(n-1)
            return
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        