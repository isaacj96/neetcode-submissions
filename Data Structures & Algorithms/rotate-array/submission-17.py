class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        n = len(nums)
        res = [0] * n
        k = k % n
        while l <= r:
            # if l + k > (n - 1):
            #     diff = (l + k) - n
            #     res[diff] = nums[l]

            # elif l + k <= (n - 1):
            res[(l + k) % n] = nums[l]
            res[(r + k) % n] = nums[r]
            l += 1
            r -= 1
        nums[:] = res