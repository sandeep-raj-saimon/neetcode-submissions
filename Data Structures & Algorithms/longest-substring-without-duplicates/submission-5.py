class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        m = {}
        count = 0
        max_count = float('-inf')

        for i,e in enumerate(s):
            if m.get(e) is None:
                count+=1
                m[e] = i
            else:
                # print(m, count, max_count)
                max_count = max(max_count, count)
                found_i = m.get(e)
                for j in range(i-count, found_i+1):
                    del m[s[j]]
                m[e] = i
                count = i - found_i
                # print(m)
        return max(max_count, count)