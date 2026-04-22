class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.checkPal(l + 1, r, s) or\
                self.checkPal(l, r - 1, s)
            l += 1
            r -= 1
        return True

    def checkPal(self, l: int, r: int, s: str) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True