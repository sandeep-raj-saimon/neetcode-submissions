class Solution:
    def countSubstrings(self, s: str) -> int:
        count = n = len(s)
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
                        count+=1

        return count