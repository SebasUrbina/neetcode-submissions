class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])


        for row in matrix:
            # do binary search

            l, r = 0, len(row) - 1

            while l<=r:

                m = l + ((r-l)//2)

                if target > row[m]:
                    l = m + 1
                elif target < row[m]:
                    r = m - 1
                else:
                    return True
        return False