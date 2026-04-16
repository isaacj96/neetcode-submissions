class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")
        if "?" in s:
            s = s.replace('?', '').strip()
            # print(s)
        if "," in s:
            s = s.replace(',', "")

        if "'" in s:
            s = s.replace("'","")

        if "." in s:
            s = s.replace(".","")
        
        if ":" in s:
            s = s.replace(":","")

        if s == s[::-1]:
            return True

        return False   