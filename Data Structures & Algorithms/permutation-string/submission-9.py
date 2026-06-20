from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        n2 = len(s2)

        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for e in s1:
            m1[e] +=1
        
        for i,e in enumerate(s2):
            m2[e] +=1
            if i >= len(s1)-1:
                match = True
                for s in s1:
                    # match = True
                    if m1.get(s) != m2.get(s):
                        match = False
                        break
                if match:
                    return True
                m2[s2[i-len(s1)+1]]-=1
        return False