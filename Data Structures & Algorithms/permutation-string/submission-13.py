class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        n1 = len(s1)
        n2 = len(s2)

        m1 = {}
        m2 = {}

        for i in range(ord('a'), ord('z')+1):
            m1[chr(i)] = 0
            m2[chr(i)] = 0

        for e in s1:
            m1[e] +=1

        for i,e in enumerate(s2):
            m2[e] +=1
            if i >= len(s1)-1:
                match = True
                for j in range(ord('a'), ord('z')+1):
                    if m1[chr(j)] != m2[chr(j)]:
                        match = False

                if match:
                    return True
                m2[s2[i-len(s1) +1]] -=1
        return False
