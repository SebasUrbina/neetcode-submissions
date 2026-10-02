class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        nums = [-1, 0, 2, 6, 8, 10] | target = 4

        - binary search algorithm

        l = 0
        r = 6-1=5
        m = 1 + (5 - 0) // 2 -> 2

        1. [L, 0, 2, M, 8, R] | M>target?
        2. [L, 0, M|R, 6, 8, 10] | 
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m

        return -1
        