class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxcount = 0
        val = 0
        for num in nums:
            count[num] += 1
            if maxcount < count[num]:
                val = num
                maxcount = count[num]
        return val