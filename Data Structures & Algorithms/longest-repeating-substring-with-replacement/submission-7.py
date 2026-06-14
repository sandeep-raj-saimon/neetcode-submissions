from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        max_freq = 0
        count = 0
        max_count = 0
        i = 0
        j = 0
        while j < n:
            c = s[j]
            freq[c] += 1
            max_freq = max(freq[c], max_freq)
            length = j-i+1
            diff = length - max_freq
            if diff <= k:
                count += 1
            else:
                freq[s[i]] -=1
                max_freq = max(max_freq, freq[s[i]])
                i+=1
            j+=1
            max_count = max(max_count,count)
        return max_count