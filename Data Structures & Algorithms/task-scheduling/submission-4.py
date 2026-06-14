from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        time = 0
        maxHeap = [-count for count in counter.values()]
        heapq.heapify(maxHeap)

        q = []
        while maxHeap or q:
            if maxHeap:
                curr_count = heapq.heappop(maxHeap)
                curr_count +=1
                if curr_count:
                    q.append([curr_count, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])
            time+=1
        return time
