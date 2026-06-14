class Solution:
    """
    if sum is odd or len of arr is 1, then ans is False
    otherwise we need to compute
    we need to check whether there exists a subset whose sum is half of total sum of arr.
    if yes then True else False
    """
    def __init__(self):
        self.ans = False
        self.nums = None
        self.target = None

    def recurse(self, index = 0, curr_sum = 0):
        if curr_sum > self.target or self.ans or index >= len(self.nums):
            return False
        
        if curr_sum == self.target:
            self.ans = True
            return True
        return (self.recurse(index+1, curr_sum + self.nums[index]) or self.recurse(index+1, curr_sum))
        

    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        total_sum = sum(nums)
        
        if total_sum % 2 == 1:
            return False
        self.nums = nums
        self.target = int(total_sum/2)
        self.recurse()
        return self.ans
        # dp = [False for _ in range(len(nums))] 
       
        # dp = [[None for _ in range(self.target+1)] for _ in range(len(nums))]

        # for index in range(len(nums)):
        #     for curr_sum in range(0, self.target+1):
        #         if dp[index][curr_sum] is None:
        #             dp[index][curr_sum] = self.recurse(index, curr_sum)
        # print(dp)
        # return dp[-1][-1] 
                    

