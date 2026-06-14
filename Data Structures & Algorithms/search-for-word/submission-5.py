class Solution:
    def __init__(self):
        self.ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        first = word[0]
        # we will search for first word, then do the searching for rest
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row = len(board)
        col = len(board[0])

        def recurse(ptr, index, path=[]):
            # print(ptr)
            if index == len(word) or self.ans:
                self.ans = True
                return True
            x,y = ptr
            for direction in directions:
                new_x,new_y = direction[0] + x, direction[1] + y
                # print(new_x, new_y, new_x >= 0 and new_x < row and new_y >=0 and new_y < col)
                if new_x >= 0 and new_x < row and new_y >=0 and new_y < col and board[new_x][new_y] == word[index] and [new_x,new_y] not in path:
                    print(path)
                    path.append([new_x,new_y])
                    recurse([new_x, new_y], index+1, path)
                    path.pop()
            return False

        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == first:
                    if recurse([i,j], 1, [[i,j]]) or self.ans:
                        return True
        return False
