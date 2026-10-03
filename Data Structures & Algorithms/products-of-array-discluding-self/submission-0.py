class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        output[i] = is the product of all elements of nums except nums[i]
                | 1 2 4 6 |
        prefix  | 1 2 8 48 | 
        postix  | 48 48 24 6 |
        """
        prefix = [1] * len(nums) # [1, 1, 1, 1, 1]
        postfix = [1] * len(nums) # [1, 1, 1, 1, 1]

        prev = 1
        for i in range(len(nums)):
            prefix[i] = prev * nums[i]
            prev = prefix[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post * nums[i]
            post = postfix[i]
        
        r = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                r[i] = 1 * postfix[i+1]
            elif i == len(nums)-1:
                r[i] = prefix[i-1] * 1
            else:
                r[i] = prefix[i-1] * postfix[i+1]

        return r




        