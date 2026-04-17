class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        modedict = defaultdict(int)
        more = len(nums) / 3
        modeset = set()

        for i in nums:
            modedict[i] += 1
            if modedict[i] > more:
                modeset.add(i)
        
        return list(modeset)