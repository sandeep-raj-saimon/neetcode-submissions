from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        # below is the adjacency list
        m = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []
        
        def dfs(start=0, path=[]):
            # if start == len(digits):
            #     return
            if len(path) == len(digits):
                ans.append("".join(path[:]))
                return
            for end in range(start, len(digits)):
                digit = digits[end]
                letters = m.get(digit)
                for letter in letters:
                    path.append(letter)
                    dfs(end+1, path)
                    print("before path is ", path, start, end)
                    path.pop()
                    print("after path is ", path, start, end)
                    print("")
            return
        dfs()
        # print(ans)
        return ans
