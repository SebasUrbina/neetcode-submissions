class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        n = [1,2,3,4]
        t = 3

        - Two pointers approach
        
        1. [l, 2, 3, r] | while l < r | if l + r > t -> move r- | if l + r < t -> move l+
        2. [l, 2, r, 4] | 1 + 3 > t => r-
        3. [l, r, 3, 4] | l + r == t check
        """

        l, r = 0, len(numbers)-1 # (0, 3)

        while l < r:
            lNum = numbers[l]
            rNum = numbers[r]

            if lNum + rNum > target:
                r -= 1
            elif lNum + rNum < target:
                l += 1
            else:
                return [l + 1, r + 1] # 0-indexes

        return []

