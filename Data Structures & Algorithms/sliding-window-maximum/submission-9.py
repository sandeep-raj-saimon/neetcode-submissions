import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        result = []

        for i,num in enumerate(nums):
            heapq.heappush(q, (-num,i))
            if i >=k-1:
                while q[0][1] <= i-k:
                    heapq.heappop(q)
                result.append(-q[0][0])
        return result