class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r, rval in enumerate(nums):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            if rval in window:
                return True
            window.add(rval)
        return False