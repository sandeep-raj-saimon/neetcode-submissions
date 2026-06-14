from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for st in strs:
            new_st = ''.join(sorted(st))
            m[new_st].append(st)
        
        return (list(m.values()))
         