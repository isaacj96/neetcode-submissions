class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newword = ""
        i = 0
        while i < len(word1) and i < len(word2):
            newword += word1[i] + word2[i]
            i += 1
        
        if len(word1) < len(word2):
            newword += word2[i:]
        elif len(word2) < len(word1):
            newword += word1[i:]
        
        return newword