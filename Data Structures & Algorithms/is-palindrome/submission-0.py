class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        string = ""
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or s[i] in numbers:
                string += s[i]
        left = 0
        right = len(string)-1
        while (left < right):
            if (string[left] != string[right]):
                return False
            left+=1
            right-=1
        return True