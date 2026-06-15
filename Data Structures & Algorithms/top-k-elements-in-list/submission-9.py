import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], j: int) -> List[int]:
        m = defaultdict(int)
        for num in nums:
            m[num]+=1
        
        a = []
        for k,v in m.items():
            a.append((-v,k))
        heapq.heapify(a)
        print(a)
        ans = []
        for i in range(j):
            ans.append(heapq.heappop(a)[1])
        return ans

