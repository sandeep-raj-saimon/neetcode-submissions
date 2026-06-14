from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_freq = 0
        max_len = 0
        m = defaultdict(int)

        while (r < len(s)):
            index = ord(s[r]) - ord('A')
            m[index] += 1
            max_freq = max(max_freq, m[index])
            
            if ((r-l+1) - max_freq > k):
                curr_index = ord(s[l]) - ord('A')
                m[curr_index] -=1
                l+=1
            
        
            if ((r-l+1) - max_freq <= k):
                max_len = max(max_len, r-l+1)
            r+=1
        return max_len