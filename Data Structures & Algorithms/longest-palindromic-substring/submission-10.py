class Solution:
    def __init__(self):
        self.ans = 0
        self.string = None

    # recursion solution
    def palindrome(self, s, i, j):
        if j-i+1 == 1:
            if self.ans < j-i+1:
                self.ans = 1
                self.string = s[i:j+1]
            return
    
        self.palindrome(s, i+1, j)
        self.palindrome(s, i, j-1)

        if s[i] == s[j] and (j-i+1) > self.ans:
            self.ans = j-i+1
            self.string = s[i:j+1]
        
        
        return
        
    def longestPalindrome(self, s: str) -> str:


        ans = None
        length = 0
        n = len(s)

        i = 0
        j = n - 1
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            length = 1


        for curr_len in range(2, n+1):
            for i in range(n - curr_len + 1):
                j = i + curr_len - 1

                if s[i] == s[j]:
                    if curr_len == 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if curr_len > length:
                            ans = s[i:j+1]
                            length = curr_len

        return ans
        