class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for n in strs:
                if i == len(n) or n[i] != strs[0][i]:
                    return n[:i]
        return strs[0]