from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        max_freq = 0
        ans = float('-inf')
        count = defaultdict(int)

        for right in range(len(s)):
            count[s[right]]+=1
            max_freq = max(max_freq, count[s[right]])

            while ((right - left + 1) - max_freq > k):
                # window is valid
                count[s[left]]-=1
                left+=1
            
            ans = max(ans, (right-left+1))
        return ans