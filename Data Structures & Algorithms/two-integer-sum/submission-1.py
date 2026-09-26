class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        # Brute for approach
        # Time: O(n2)
        # for i in len(nums):
        #     for j in len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Efficient approach: hash table
        # Time: O(n)
        seen = {}
        # [4,5,6]
        # 1. (0, 4) | v=10 | {4: 0}
        # 2. (1, 5) | v=5  | {5: 1}
            # 4 is in {0: 4} => check
        # 3. (2, 6) | v=4  | {4: 2}
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], idx]
            seen[num] = idx
        
        return []

            












        