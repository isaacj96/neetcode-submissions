class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat = [0] * (2 * n)
        for i, num in enumerate(nums):
            concat[i] = concat[i + n] = num
        return concat