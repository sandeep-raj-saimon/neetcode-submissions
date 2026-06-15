class Solution:
    MOD = 256
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for str in strs:
            for s in str:
                encoded_str += chr((ord(s) - ord('a')) % 256)
            encoded_str += '#'
        return encoded_str
    def decode(self, s: str) -> List[str]:
        ans = []
        s = s.split('#')

        for i in s[:-1]:
            m = ''
            for j in i:
                m += chr((ord(j) + ord('a')) % 256)
            ans.append(m)
        return ans