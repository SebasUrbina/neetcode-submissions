class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Daily temperatures
        # result[i] numbers of days after the ith day before a warner temperature on future.
        # numero de dias despues del i-esimo dia antes de una tempatura mas alta
        """
          0    1    2    3    4    5   6
        | 30 - 38 - 30 - 36 - 35 - 40 -28 |
        | 1               i

        2 - 1 - 1 - 3
                    ith
        2 - 1 - 1


        i(0) = 30 -> 1
        i(1)= 38 -> 4 [30, 36, 35, "40"]
        i(2)= 30 -> 1
        i(3)= 36 -> 2
        i(4)= 35 -> 1
        i(5)= 40 -> 0
        i(5)= 40 -> 0

        for each ith day we look to the future and count until we get higher temperature

        currentT = 

        if we stop (in the future) at ith day. 
        stack LIFO
        """
        #  Brute force approach
        # n = len(temperatures)
        # res = [0] * n

        # for i in range(n):
        #     currT = temperatures[i] # ith
        #     counts = 1
        #     for j in range(i+1, n): # we look to the future
        #         futureT = temperatures[j]
        #         if futureT > currT:
        #             res[i] = counts
        #             break # we need the first occurrence
        #         counts += 1
        # return res

        # we'll store the days waiting for a greater temperature. (indexes)

        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop() # LIFO
                res[prev_i] = i - prev_i

            stack.append(i)
        return res                
















        