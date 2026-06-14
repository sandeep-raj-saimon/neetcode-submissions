import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        count = 0
        while(count < k-1):
            heapq.heappop(nums)
            count+=1
        return -nums[0]