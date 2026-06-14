class Solution:
    def findPivot(self, arr):
        low = 0
        high = len(arr) - 1

        while(low < high):
            mid = (low+ high)//2

            if mid > low and mid < high and arr[mid] < arr[mid-1] and arr[mid] < arr[mid+1]:
                return mid
            
            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid + 1
        return high
    def binarySearch(self, arr, target, low, high):
        while (low <= high):
            mid = (low + high)//2

            if arr[mid] == target:
                return mid

            if arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        print(pivot)
        if nums[pivot] == target:
            return pivot
        if nums[pivot] < target <= nums[-1]:
            return self.binarySearch(nums, target, pivot + 1, len(nums)-1)
        else:
            return self.binarySearch(nums, target, 0, pivot - 1)