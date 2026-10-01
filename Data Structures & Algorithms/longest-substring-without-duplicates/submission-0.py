class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        
        x y z z x y z
        l 
        r

        """

        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        
        return res
                























