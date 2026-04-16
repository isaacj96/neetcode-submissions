class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) != 0:
            tmp = []
            seq = []
            nums = sorted(list(set(nums)))
            for i in range(len(nums)):
                if i < len(nums) - 1:
                    if nums[i] + 1 == nums[i+1]:
                        tmp.append(nums[i])
                    else:
                        tmp.append(nums[i])
                        if len(tmp) > len(seq):
                            seq = tmp[:]
                        tmp = []
                else:
                    tmp.append(nums[i])
                    if len(tmp) > len(seq):
                        seq = tmp[:]
            
            return(len(seq))
        return len(nums)