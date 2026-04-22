class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        COLS = len(matrix[0])
        ROWS = len(matrix)
        start = 0
        end = ROWS * COLS -1
        while start <= end:
            middle = start + (end - start ) // 2
            row  = middle // COLS
            col  = middle % COLS
            if target > matrix[row][col]:
                start = middle + 1
            elif target < matrix[row][col]:
                end = middle -1 
            else:
                return True
        return False

        