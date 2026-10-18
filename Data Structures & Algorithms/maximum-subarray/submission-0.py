class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums:      2 -3 4 -2 2 1 -1 4 

        # 1. -> 2
        # 2. -> -1 # does this value contribute to the overall? ignore
        # 3. -> 4 

        # T: O(n)
        # S: O(1)
        currSum = 0
        maxSum = nums[0]
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num

            maxSum = max(maxSum, currSum)
        return maxSum


        