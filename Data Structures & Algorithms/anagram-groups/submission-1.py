class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        m = {}
        for s in strs:
            i = ''.join(sorted(s))
            if m.get(i) is None:
                m[i] = [s]
            else:
                m[i].append(s)
        ans = []
        for val in m.values():
            ans.append(val)
        return ans