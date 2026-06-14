class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]

        stack = []
        for i in range(n):
            a = arr[i]
            count = 0
            while stack and a <= arr[stack[-1]]:
                count+= max_left[stack.pop()]+1
            max_left[i] = count
            stack.append(i)

        stack = []
        for i in range(n-1, -1,-1):
            a = arr[i]
            count = 0
            while stack and a <= arr[stack[-1]]:
                count+= max_right[stack.pop()]+1
            max_right[i] = count
            stack.append(i)
        print(max_left, max_right)

        max_ans = 0
        for i in range(n):
            ans = arr[i] * (max_left[i] + max_right[i] + 1)
            max_ans = max(ans, max_ans)
        return max_ans
