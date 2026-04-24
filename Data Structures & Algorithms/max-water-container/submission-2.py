class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        tmp = 0

        while l < r:
            width = r - l
            length = min([heights[r], heights[l]])
            tmp = width * length
            if tmp > area:
                area = tmp

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area