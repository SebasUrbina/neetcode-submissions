class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We should know about Two Sum II (sorted array) in this case we use a while loop
        
        nums = [-1,0,1,2,-1,-4]

        """
        nums.sort() # sorted array [-4, -1, -1, 0, 1, 2]
        triplets = []
        # i, l, r (three points, i is looked and on the rest we solve two sums II. 
        for i, ni in enumerate(nums):
            # We ignore cases where we have equals n[i]...
            if i > 0 and nums[i-1] == ni:
                continue
            
            # We start on 1 because n[i] is looked
            l, r = i + 1, len(nums) - 1

            while l < r:
                # Thank to the array is sorted...
                threeSum = ni + nums[l] + nums[r] # ni + nl + nr = 0

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # We could have this problem
                    # [-1, -1 , 0, 1, 2]
                    triplets.append([ni, nums[l], nums[r]])
                    # From left to right we need to avoid duplicates
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return triplets



        

        