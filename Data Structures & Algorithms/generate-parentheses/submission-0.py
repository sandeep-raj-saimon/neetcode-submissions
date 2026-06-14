class Solution:
    def generate(self, ans, string, score, n):
        if score < 0:
            return
        if score == 0 and len(string) == n*2:
            ans.append(string)
        if len(string) == n*2:
            return
        self.generate(ans, string + "(", score +1, n)
        self.generate(ans, string + ")", score -1, n)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        string= "("
        score = 1
        self.generate(ans, string + "(",  score+1, n )
        self.generate(ans, string + ")", score-1, n )
        return ans