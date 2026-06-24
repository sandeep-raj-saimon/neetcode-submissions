class Solution:
    def findIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return left
    def binarySearch(self, nums: List[int], target) -> int:
        print(nums)
        left = 0
        n = len(nums)
        right = n-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >target:
                right = mid-1
            else:
                left = mid+1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        point = self.findIndex(nums)
        print(point)
        # return point
        if point != 0:
            if nums[point] == target:
                return point
            elif target <= nums[-1]:
                index = self.binarySearch(nums[point:], target)
                if index == -1:
                    return -1
                return point + self.binarySearch(nums[point:], target)
            else:
                return self.binarySearch(nums[:point], target)
        else:
            return self.binarySearch(nums, target)
