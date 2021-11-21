#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#


# @lc code=start
class Solution:
    def spiralOneLayer(self, matrix, x_1, y_1, x_2, y_2, ans):
        # 初始化
        i, j = x_1, y_1
        # 只有一行：
        if x_1 == x_2:
            for j in range(y_1, y_2 + 1):
                ans.append(matrix[x_1][j])
        elif y_1 == y_2:
            for i in range(x_1, x_2 + 1):
                ans.append(matrix[x_1][j])
        while j < y_2:
            ans.append(matrix[i][j])
            j += 1
        # j = y_2
        while i < x_2:
            ans.append(matrix[i][j])
            i += 1
        # i = x_2
        while j > y_1:
            ans.append(matrix[i][j])
            j -= 1
        # j = y_1
        while i > x_1:
            ans.append(matrix[i][j])
            i -= 1

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_1, y_1 = 0, 0
        x_2, y_2 = len(matrix) - 1, len(matrix[0]) - 1
        ans = []

        while x_1 < x_2 or y_1 < y_2:
            self.spiralOneLayer(matrix, x_1, y_1, x_2, y_2, ans)
            x_1 += 1
            y_1 += 1
            x_2 -= 1
            y_2 -= 1
        return ans


matrix = [[6, 9, 7]]
# @lc code=end
