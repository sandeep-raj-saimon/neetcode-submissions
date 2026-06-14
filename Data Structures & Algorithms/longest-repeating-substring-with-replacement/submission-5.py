class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        freq = defaultdict(int)
        max_freq = 0
        ans = 0
        n = len(s)
        while(j < n) :
            str = s[j]
            freq[s[j]] +=1
            window = j - i + 1

            max_freq = max(max_freq, freq[str])

            if window - max_freq <= k:
                ans = max(ans, window)
            else:
                freq[s[i]] -=1
                i+=1
            
            j+=1
        return ans