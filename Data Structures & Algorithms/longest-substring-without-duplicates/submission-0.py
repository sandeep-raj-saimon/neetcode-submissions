class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        max_count = float('-inf')
        count = 0

        left = 0
        right = 0

        while (right < len(s)):
            string = s[right]

            if m.get(string) is None:
                m[string] = right
                count+=1
            else:
                index = m.get(string)
                while(left <= index):
                    m[s[left]] = None
                    left+=1
                m[string] = right
                max_count = max(count, max_count)
                count = right - index
                print(count, string, right, index)
            right +=1
        print(m)
        return max(count, max_count)