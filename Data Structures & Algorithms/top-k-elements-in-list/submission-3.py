from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = [[-count, item] for item,count in counter.items()]
        heapify(counter)
        ans = []
        for i in range(k):
            ans.append(heappop(counter)[1])
        return ans
