class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        pos = -1
        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                pos = mid
                l = mid+1
            else:
                r = mid-1
        return pos+1