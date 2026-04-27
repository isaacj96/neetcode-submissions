class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            for j, num1 in enumerate(nums):
                if num == num1 and abs(i - j) <= k and i != j:
                    return True

        return False