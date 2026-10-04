class Solution:
    def trap(self, height: List[int]) -> int:
        """
        La restriccion para atrapar agua es 
        
        left = [...]
        right = [...]
        leftMax = max[left]
        rightMax = max[right]

        waterAtI = min(leftMax, rightMax) - height[i]

        waterAtI = max(waterAtI, 0)

        # [0, 2, 0, 3] -> leftMax[]
        """

        # Brute force
        # water = 0

        # leftMax = 0
        # rightMax = 0
        # for i in range(1, len(height)-1):
        #     leftMax = max(height[:i])
        #     rightMax = max(height[i+1:])

        #     water += max(min(leftMax, rightMax) - height[i], 0)
        # return water

        water = 0
        n = len(height)
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * n
        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        
        for i in range(n):
            water += max(min(leftMax[i], rightMax[i]) - height[i], 0)


        return water

