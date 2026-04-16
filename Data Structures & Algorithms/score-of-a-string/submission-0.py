class Solution:
    def scoreOfString(self, s: str) -> int:
        sumascci = 0
        for i in range(len(s)):
            if i < len(s)-1:
                sumascci += abs(ord(s[i+1]) - ord(s[i]))
        return sumascci