class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if m.get(num) is not None:
                m[num] +=1
            else:
                m[num] = 1
        
        x =  {k: v for k, v in sorted(m.items(), key=lambda item: -item[1])}

        ans = []
        for i in x:
            if len(ans) < k:
                ans.append(i)

        return ans