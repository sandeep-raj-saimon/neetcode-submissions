from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = defaultdict(int)
        for i in s:
            m[i] +=1

        for j in t:
            m[j] -=1
        for k,v in m.items():
            if v != 0:
                return False

        return True