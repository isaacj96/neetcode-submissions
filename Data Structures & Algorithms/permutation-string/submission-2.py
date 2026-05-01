class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
        s2Count = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}

        for i, _ in enumerate(s1):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        matches = 0
        for key in s1Count:
            print(key)
            if s1Count[key] == s2Count[key]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            r_val = s2[r]
            s2Count[r_val] += 1
            if s1Count[r_val] == s2Count[r_val]:
                matches += 1
            elif s1Count[r_val] + 1 == s2Count[r_val]:
                matches -= 1
            
            l_val = s2[l]
            s2Count[l_val] -= 1
            if s1Count[l_val] == s2Count[l_val]:
                matches += 1
            elif s1Count[l_val] - 1 == s2Count[l_val]:
                matches -= 1
            l += 1

        return matches == 26
            
