class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we need to count each char appearning
        sorted_s = ''.join(sorted(s)) # [s1, s2, ..., sn]
        sorted_t = ''.join(sorted(t)) # [t1, t2, ..., tn] 
        # Compare arrays
        if sorted_s != sorted_t:
            return False
        
        return True

