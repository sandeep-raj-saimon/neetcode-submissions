class Solution:
    def __init__(self):
        self.ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        def dfs(i, j, k):
            if k >= len(word):
                return True
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] ==True or board[i][j] != word[k]:
                return False
            visited[i][j] = True
            res = (dfs(i, j+1, k+1) or dfs(i, j-1, k+1) or dfs(i-1, j, k+1) or dfs(i+1, j, k+1))
            visited[i][j] = False
            return res           
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False