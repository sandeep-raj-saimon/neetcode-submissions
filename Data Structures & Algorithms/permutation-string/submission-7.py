from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if len(s1) > len(s2):
            return False

        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for s in s1:
            m1[s] +=1
        
        for i in range(len(s2)):
            m2[s2[i]]+=1
            if i >= len(s1)-1:
                print(m2, i, s2[i])
                is_match = True
                # print(m1, m2)
                for s in s1:
                    if m1.get(s) != m2.get(s):
                        is_match = False
                        break
                if is_match:
                    return True
                m2[s2[i-len(s1)+1]] -= 1
                print(m2, i, s2[i])
        return False

            
