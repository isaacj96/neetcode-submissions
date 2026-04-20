class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lowest_number = 1
        nums = sorted(nums)
        for num in nums:
            if lowest_number == num:
                lowest_number += 1
        return lowest_number