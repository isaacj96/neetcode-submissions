class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        myChars = [0] * 26
        for i in range(len(s)):
            myChars[ord(s[i]) - ord('a')] += 1
            myChars[ord(t[i]) - ord('a')] -= 1
        
        for i in myChars:
            if i != 0:
                return False
        return True