class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
            A           B
            3           2

        trA = (10-1)/3 = 3
        trB = (10-4)/2 = 4
        
        trA < trB and A < B => 1 fleet, porque se intersectan

        if tL < tR:
            => 1 fleet, they catch up

        if tL > tR:
            => 2 fleet, never catch up
        """
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        # desde el mas cercano al mas lejano

        stack = []
        for pos, speed in cars: # from the farthest to the nearest
            time = (target - pos)/speed # time this card should take to get the target

            if not stack:
                stack.append(time)
            elif stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)

            

        