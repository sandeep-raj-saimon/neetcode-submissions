from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], j: int) -> List[int]:
        m = defaultdict(int)

        for num in nums:
            m[num]+=1
        
        m = dict(sorted(m.items(), key=lambda item: -item[1]))
        ans = []
        count = 0
        for k,v in m.items():
            if count < j:
                ans.append(k)
                count+=1
            else:
                break

        return ans
