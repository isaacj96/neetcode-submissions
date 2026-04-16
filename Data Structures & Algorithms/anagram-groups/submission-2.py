class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        for word in strs:
            # print(f"Word: {word}")
            ordered_str = ''.join(sorted(word))
            # print(f"Ordered Str: {ordered_str}")
            matches[ordered_str].append(word)
        
        return list(matches.values())
