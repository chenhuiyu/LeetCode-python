#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False

        # 第一行是否要变0
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
# 第一列是否要变0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        # 遍历数组，如果i,j位置是0，标记i行和j列为0，记录到第0行和第0列中
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 再次遍历数组（除第0行和第0列外），如果第0行或者第0列标记的是0，把i,j位置变0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
# 如果第0行的标记是0，把第零行变0
        if first_row_zero is True:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
# 如果第0列的标记是0，把第0列变0
        if first_col_zero is True:
            for i in range(len(matrix)):
                matrix[i][0] = 0


# @lc code=end
