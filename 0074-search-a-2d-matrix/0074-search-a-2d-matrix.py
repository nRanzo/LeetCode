class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # edge case too small
        if target < matrix[0][0]:
            return False

        # row finder
        top, bottom = 0, m - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                top = mid_row + 1
            else:
                bottom = mid_row - 1

        row = bottom
        
        # column finder
        left, right = 0, n - 1
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return False