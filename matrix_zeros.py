# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_locations = []
        zero_rows = {}
        zero_cols = {}
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_locations.append([i, j])

        if not any(zero_locations):
            return

        for location in zero_locations:
            row_no = location[0]
            col_no = location[1]
            if row_no not in zero_rows:
                for i in range(0, col_len):
                    matrix[row_no][i] = 0
                    zero_rows[row_no] = 1

            if col_no not in zero_cols:
                for i in range(0, row_len):
                    matrix[i][col_no] = 0
                    zero_cols[col_no] = 1
