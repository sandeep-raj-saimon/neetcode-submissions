class Solution:
    def findPivot(self, nums):
        low  = 0
        high = len(nums) - 1
        # we are using low < high, as it not garaunteed that there exists a pivot point
        while low < high:
            mid = (low+high)//2

            # this is the pivot point
            if mid > low and mid < high and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return mid

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return high
    def findMin(self, nums: List[int]) -> int:
        index = self.findPivot(nums)
        return nums[0] if index == -1 else nums[index]