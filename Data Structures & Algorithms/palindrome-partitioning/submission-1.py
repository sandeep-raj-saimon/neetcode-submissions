class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(s):
            return s == s[::-1]

        res = []
        def recurse(start=0, path=[]):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start+1, len(s)+1):
                string = s[start:end]
                if isPalindrome(string):
                    path.append(string)
                    recurse(end, path)
                    path.pop()
        recurse()
        return res