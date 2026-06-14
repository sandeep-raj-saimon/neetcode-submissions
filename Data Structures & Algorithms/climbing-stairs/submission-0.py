class Solution:
    def findWays(self, steps):
        if steps == 0:
            return 0
        elif steps == 1:
            return 1
        elif steps == 2:
            return 2
        else:
            return (self.findWays(steps - 1) + self.findWays(steps-2))
    def climbStairs(self, n: int) -> int:
        if n == 0 or n ==1 or n == 2:
            return n

        steps = [0] * (n+1)
        for i in range(3):
            steps[i] = i
        
        for i in range(3,n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]