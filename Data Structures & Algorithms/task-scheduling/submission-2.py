from collections import Counter
import heapq
class Solution:
    def __init__(self):
        self.maxHeap = None
        self.interval = None
    def getTime(self):
        # cases to be covered
        # in beginning, maxHeap, would contain all task's frequencies
        # the element with max freq will be executed first and will be popped from maxHeap
        # in order ot keep track of its next execution, we are maintaining a queue
        # hence maxHeap can be empty as well as queue can be empty
        heapq.heapify(self.maxHeap)
        q = []
        time = 0
        while self.maxHeap or q:
            time+=1
            if self.maxHeap:
                count = 1 + heapq.heappop(self.maxHeap)
                if count:
                    q.append([count, time + self.interval])
            
            if q and q[0][1] == time:
                heapq.heappush(self.maxHeap, q.pop(0)[0])
    
        return time
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        self.maxHeap = [-i for i in counter.values()]
        self.interval = n
        return self.getTime()