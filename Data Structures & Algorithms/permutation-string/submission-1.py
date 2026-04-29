class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = [0] * 26
        s2count = [0] * 26

        # 1. Initialize the first window
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        # 2. Count initial matches
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        
        # 3. Slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add right character
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]: # Just became unequal
                matches -= 1

            # Remove left character
            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]: # Just became unequal
                matches -= 1
            l += 1
            
        return matches == 26