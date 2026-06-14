class Solution:
    def findPivot(self, nums):
        low = 0
        high = len(nums)-1

        while(low < high):
            mid = (low+high)//2

            if mid > low and mid < high and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return mid
            
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1

        return high
    def findMin(self, nums: List[int]) -> int:
        pivot = self.findPivot(nums)
        return nums[pivot] if pivot != -1 else nums[0]
        