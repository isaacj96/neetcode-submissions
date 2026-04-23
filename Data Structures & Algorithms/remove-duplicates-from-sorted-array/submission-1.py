class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for i in range(len(nums)):
            if nums[i] in unique:
                pass
            else:
                unique.append(nums[i])
        nums[:len(unique)] = unique
        return len(unique)
        
        