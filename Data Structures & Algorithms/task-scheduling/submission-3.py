from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        """
        counter = Counter(tasks)
        maxHeap = [-i for i in counter.values()]
        heapq.heapify(maxHeap)
        q = []
        time = 0

        while maxHeap or q:
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])

                
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])

            time+=1
        return time