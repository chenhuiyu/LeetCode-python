#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_1, y_1 = 0, 0
        x_2, y_2 = len(matrix), len(matrix[0])

        while x_1 < x_2 and y_1 < y_2:
            spiralOneLayer(matrix, x_1, y_1, x_2, y_2)
            x_1 += 1
            y_1 += 1
            x_2 -= 1
            y_2 -= 1

        def spiralOneLayer(matrix, x_1, y_1, x_2, y_2):
            i, j = x_1, y_1


# @lc code=end
