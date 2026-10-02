class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1

        while top <= bot:
            row = top + ((bot-top)//2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top<=bot):
            return False
        
        row = matrix[top + ((bot-top)//2)]
        l, r = 0, cols - 1
        while l<=r:

            m = l + ((r-l)//2)

            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True
        return False