class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. Count the occurrences of each element in the num array
        2. {"e1": c1, "e": c2,.., }
        # select the top k most common (sorting the dictionary)
        """
        # from collections import defaultdict
        # counts = defaultdict(list)
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 0

            counts[num] += 1
            # {1:1, 2:2, 3:3} -> (k=2) -> [2,3]
            # sort the dictionary
        
        # sorted(counts.items(), key= lambda x: x[1]) -> list
        # sorted by the key element in descending order: {'a': 10}
        sortedListDesc = sorted(counts.items(), key= lambda x: x[1], reverse=True)

        topK = list(map(lambda x: x[0], sortedListDesc))[:k]

        return topK

                        
