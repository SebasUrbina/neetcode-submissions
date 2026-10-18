class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # a(i,j) = (j-1)*min(height[i], height[j])
        # a(i, j+1) > a(i, j)

        l, r = 0, len(heights) - 1
        res = 0
        while l < r:

            area = (r - l)*min(heights[l], heights[r]) # amount of water
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
        return res



        