class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        count = 0
        if len(nums) == 0 or len(nums) == 1:
            return False
        for i in nums:
            for j in nums:
                if i == j:
                    count +=1
            mydict[i] = count
            count = 0
        for i in mydict.values():
            if i > 1:
                return True
        return False