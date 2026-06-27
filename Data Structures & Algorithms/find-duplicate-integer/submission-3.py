class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if nums[abs(num)%n] < 0:
                return abs(num)
            
            nums[abs(num)] = -nums[abs(num)]
        return -1