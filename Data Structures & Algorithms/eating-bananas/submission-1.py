class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # los candidatos van de [1, ..., max(piles)]
        # [1, 2, 3, 4, mid, 6, 7]
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left



        