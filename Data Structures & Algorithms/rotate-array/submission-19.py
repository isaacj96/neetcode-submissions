class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        n = len(nums)
        # res = [0] * n
        k = k % n
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        # while l <= r:
        #     # res[(l + k) % n] = nums[l]
        #     nums[(l + k) % n], nums[l] = nums[l], nums[(l + k) % n]
        #     nums[(r + k) % n], nums[r] = nums[r], nums[(r + k) % n]
        #     l += 1
        #     r -= 1
