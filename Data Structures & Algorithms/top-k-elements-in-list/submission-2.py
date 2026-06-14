from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        arr = [[] for i in range(len(nums)+1)]
        for key, value in freq.items():
            arr[value].append(key)

        res = []

        for i in arr[::-1]:
            for num in i:
                res.append(num)
                if len(res) == k:
                    return res
