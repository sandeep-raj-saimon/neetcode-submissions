class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        m = {}
        count = 0
        max_count = float('-inf')
        while right < len(s):
            string = s[right]
            if m.get(string) is None or m.get(string) < left:
                m[string] = right
                count+=1
            else:
                left = m.get(string)+1
                m[string] = right
                count = right - left + 1
            max_count = max(max_count, count)
            right+=1
        return max_count if max_count != float('-inf') else 0