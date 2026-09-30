class Solution:
    def isPalindrome(self, s: str) -> bool:

        r = ""
        for c in s:
            if c.isalnum():
                r += c.lower()
        return r == r[::-1]



        