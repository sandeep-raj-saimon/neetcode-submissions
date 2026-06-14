class Solution:
    def climbStairs(self, n: int) -> int:
        """
        we have 2 options
        to climb 1 stair or 2 stair
        """

        if n ==1 or n == 2:
            return n
        arr = [0 for _ in range(n)]
        arr[0] = 1
        arr[1] = 2

        for i in range(2,n):
            print(i)
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]
        

        