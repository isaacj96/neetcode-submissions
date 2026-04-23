class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for i in range(len(nums)):
            if nums[i] in unique:
                # print(f"In if statement: {nums[i]}")
                pass
            else:

                # print(nums[i])
                unique.append(nums[i])
        # print(count)
        nums[:len(unique)] = unique
        return len(unique)
        
        