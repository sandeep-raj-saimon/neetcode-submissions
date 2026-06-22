import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        result = []
        # 4,2,1,4,1,2,1
        # 0,1,2,3,4,5,6
        # k = 3
        """
        when i is at 2, we need to start finding the max
        starting element of heap is the max
        lets say i is at 2
        max will be 4, present at 4
        """
        for i, num in enumerate(nums):
            heapq.heappush(q, (-num, i))

            if i >= k-1:
                # we are removing all the top elements if they lie
                # outside the window
                # we are not doing just "="
                # cause after popping, next element would become largest
                # but if that too is outside window, we need to pop it
                # hence we use while and <=
                while q[0][1] <= i-k:
                    heapq.heappop(q)
                result.append(-q[0][0])
        return result