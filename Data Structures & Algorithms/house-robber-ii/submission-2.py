class Solution:
    def helper(self, arr):
        arr[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            arr[i] = max(
                arr[i] + arr[i-2],
                arr[i-1]
            )
        return arr[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        arr1 = arr2 = nums[:]
        profit1 = self.helper(arr1[:-1])
        profit2 = self.helper(arr2[1:])

        return max(profit1, profit2)

        