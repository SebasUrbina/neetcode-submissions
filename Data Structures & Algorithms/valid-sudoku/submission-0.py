class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    #    board = \
    #     [
    #         ["1","2",".",".","3",".",".",".","."],
    #         ["4",".",".","5",".",".",".",".","."],
    #         [".","9","8",".",".",".",".",".","3"],
    #         ["5",".",".",".","6",".",".",".","4"],
    #         [".",".",".","8",".","3",".",".","5"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".",".",".",".",".",".","2",".","."],
    #         [".",".",".","4","1","9",".",".","8"],
    #         [".",".",".",".","8",".",".","7","9"]
    #     ]

        # Brute force approach
        # for i in range(9): # row
        #     rowNums = [n for n in board[i] if n != "."]
        #     uniqueNums = len(set(rowNums))
        #     # duplicates?
        #     if len(rowNums) != uniqueNums:
        #         return False
        
        # for j in range(9):
        #     colNums = [board[i][j] for i in range(9) if board[i][j] != "."]
        #     uniqueNums = len(set(colNums))
        #     # duplicates?
        #     if len(colNums) != uniqueNums:
        #         return False

        # for k in range(9):
        #     row = (k // 3) * 3
        #     col = (k % 3) * 3

        #     box = [
        #         board[r][c]
        #         for r in range(row, row+3)
        #         for c in range(col, col+3)
        #     ]

        #     boxNums = [n for n in box if n != "."]
        #     uniqueNums = len(set(boxNums))
        #     if len(boxNums) != uniqueNums:
        #         return False

        # return True

        # Optimized
        for k in range(9):
            row = (k // 3) * 3
            col = (k % 3) * 3
            seen = set()

            # Boxes
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)

            seen = set()
            rowNums = [val for val in board[k] if val != "."]
            for num in rowNums:
                if num in seen:
                    return False
                seen.add(num)

            seen = set()
            colNums = [board[j][k] for j in range(9) if board[j][k] != "."]
            for num in colNums:
                if num in seen:
                    return False
                seen.add(num)
        return True
