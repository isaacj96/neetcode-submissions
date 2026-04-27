class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        n = len(height)
        l = 0
        r = n - 1

        maxleft = height[l]
        maxright = height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxleft = max(height[l], maxleft)
                res += maxleft - height[l]
            else:
                r -= 1
                maxright = max(height[r], maxright)
                res += maxright - height[r]
        
        return res