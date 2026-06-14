class Solution:
    def ptRotation(self, nums):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = (left+right)//2

            if mid < right and nums[mid] > nums[mid]+1:
                return mid+1
            if mid > left and nums[mid] < nums[mid-1]:
                return mid

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid -1
        return mid

    def search(self, nums: List[int], target: int) -> int:
        index = self.ptRotation(nums)
        if nums[index] == target:
            return index
        elif nums[index] < target <= nums[-1]:
            left = index+1
            right = len(nums)-1
        else:
            left = 0
            right = index-1
        print(left, right, index)
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1