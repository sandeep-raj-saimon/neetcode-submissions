from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        we will use 2 pointers and sliding windown technique for solving this
        """

        left = 0
        right = 0
        freq = defaultdict(int)
        max_len = 0
        max_freq = 0
        while (right < len(s)):
            curr_len = right - left + 1
            index = ord(s[right]) - ord('A')
            freq[index]+=1

            max_freq = max(max_freq, freq[index])

            if (curr_len - max_freq <= k): #valid window
                max_len = max(max_len, curr_len)
            else:
                new_index = ord(s[left]) - ord('A')
                freq[new_index] -=1
                left +=1
            right +=1
        return max_len

