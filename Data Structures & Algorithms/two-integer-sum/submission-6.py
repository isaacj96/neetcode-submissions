class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                # print(nums[i], nums[j])
                if nums[i] + nums[j] == target and i != j:
                    arrayindex = []
                    arrayindex.append(i)
                    arrayindex.append(j)
                    return arrayindex
        return nums