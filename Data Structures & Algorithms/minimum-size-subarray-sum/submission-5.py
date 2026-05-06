class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        l = 0

        for r, rval in enumerate(nums):
            total += rval
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
    
        return 0 if res == float('inf') else res