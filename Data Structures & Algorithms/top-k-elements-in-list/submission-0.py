from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        ans = []

        for num in nums:
            m[num] +=1

        m = dict(sorted(m.items(), key=lambda item: item[1], reverse = True))
        for key, value in m.items():
            ans.append(key)
            if (len(ans) == k):
                break
        return ans
        