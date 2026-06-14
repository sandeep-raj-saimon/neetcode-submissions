class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        bruteforce approach would be to generate all substrings and check if they are palindrome or not
        1. I may select a character or may not select a character
        2. substring can be of length 1 and can upto the length of string
        """
        
        def isPalindrome(s):
            return s == s[::-1]

        res = []
        def backTrack(start=0,path=[]):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start+1, len(s)+1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)
                    backTrack(end, path)
                    path.pop()
            return
        backTrack()
        return res
        