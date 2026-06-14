class Solution:
    def findPivot(self, nums):
        left = 0
        right = len(nums)-1

        while (left < right):
            mid = (left+right)//2
            if mid > left and mid < right and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return mid


            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return right

    def findMin(self, nums: List[int]) -> int:
        index = self.findPivot(nums)
        return nums[index] if index != -1 else nums[0]
        