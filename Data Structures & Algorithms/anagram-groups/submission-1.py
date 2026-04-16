class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        for string in strs:
            ordered_string = ''.join(sorted(string))
            matches[ordered_string].append(string)
    
        return matches.values()
        