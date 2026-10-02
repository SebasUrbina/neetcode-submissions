class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
        "2" 3 4 5         "10"        "20"
        2, 10, 20 -> start sequence numbers

        5, 4, 3, 2 have left number => sequence

        1. está el predecesor en el conjunto?
        2. num es un start sequence
        3. busco si está el resto de secuencia (iterativamente)
        """
        nums = set(nums)
        maxSequence = 0
        for num in nums:
            if (num - 1) not in nums: # doest it have a start?
                k = num
                currentMax = 0
                while k in nums: # O(1)
                    k += 1
                    currentMax += 1
                    maxSequence = max(maxSequence, currentMax)

        return maxSequence
                    
