class Solution:
    def findPivot(self, arr):
        low = 0
        high = len(arr) - 1

        while(low < high):
            mid = (low + high)//2
            if mid > low and mid < high and arr[mid] < arr[mid-1] and arr[mid] < arr[mid]+1:
                return mid
            
            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid + 1
        return high
    def findMin(self, nums: List[int]) -> int:
        pivot = self.findPivot(nums)
        if pivot == -1:
            return nums[0]
        return nums[pivot]