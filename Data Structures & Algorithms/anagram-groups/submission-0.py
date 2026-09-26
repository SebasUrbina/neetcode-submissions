class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # {'abc': ['acb', 'bac]} # group of anagram abc
        for s in strs: # O(m*nlogn)
            sortedS = ''.join(sorted(s)) # "abc", canonical anagram
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS] += [s]
        return list(res.values())

        # from collections import defaultdict
        # res = defaultdict(list) -> {each-key: []}
        # res['something'].append(new_value)

        