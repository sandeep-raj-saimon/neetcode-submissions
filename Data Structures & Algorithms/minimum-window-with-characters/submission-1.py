from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        m = defaultdict(int)
        n = len(s)
        count = 0
        ans = float('inf')
        ans_start = 0
        for e in t:
            m[e] +=1
            count+=1

        while r < n:
            e = s[r]
            m[e] -=1

            if m[e] >= 0:
                count-=1
            
            while count == 0:
                if r -l +1 <ans:
                    ans = r-l+1
                    ans_start = l
                
                m[s[l]] +=1
                if m[s[l]] > 0:
                    count+=1

                l+=1
            r+=1
        if ans == float('inf'):
            return ""
        return s[ans_start:ans_start + ans]

        