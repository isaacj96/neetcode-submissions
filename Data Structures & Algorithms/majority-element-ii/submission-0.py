class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        modedict = defaultdict(int)
        more = len(nums) / 3
        modeset = []

        for i in nums:
            modedict[i] += 1
            if modedict[i] > more:
                modeset.append(i)
        
        return list(set(modeset))