from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 
        right = 0
        n = len(s)
        need = defaultdict(int)
        missing = 0
        ans_start = 0
        ans_length = float('inf')
        for e in t:
            need[e] += 1
            missing +=1

        while right < n:
            e = s[right]
            need[e]-=1

            if need[e]>=0:
                missing -=1

            while missing == 0:
                if right-left+1 < ans_length:
                    ans_length = right-left+1
                    ans_start = left

                need[s[left]] +=1
                if need[s[left]] > 0:
                    missing += 1
                left+=1
            right+=1
        
        if ans_length == float('inf'):
            return ""
        return s[ans_start: ans_start+ans_length]

                