#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#


# @lc code=start
class Solution:
    def rotateLayer(self, matrix, x_1, y_1, x_2, y_2):
        # 对于第k层，计算这一圈的阶数（行数和列数）
        k = x_2 - x_1 + 1
        # 假如这一圈的阶数为k，需要分成k-1个组
        # 每一组四个值的交换顺序是固定的
        for i in range(k):
            # 第i组的第1个值:matrix[x_1][y_1 + i]
            # 第i组的第2个值:matrix[x_1 + i][y_2]
            # 第i组的第3个值:matrix[x_2][y_2 - i]
            # 第i组的第4个值:matrix[x_2 - i][y_1]
            # 交换顺序1=>2 2=>3 3=>4 4=>1
            print("第", i, "组")
            # 暂时记下第4个值
            temp = matrix[x_2 - i][y_1]
            # 3=>4
            print("3=>4:", matrix[x_2 - i][y_1], "=", matrix[x_2][y_2 - i])
            matrix[x_2 - i][y_1] = matrix[x_2][y_2 - i]
            # 2=>3
            print("2=>3:", matrix[x_2][y_2 - i], "=", matrix[x_1 + i][y_2])
            matrix[x_2][y_2 - i] = matrix[x_1 + i][y_2]
            # 1=>2
            print("1=>2:", matrix[x_1 + i][y_2], "=", matrix[x_1][y_1 + i])
            matrix[x_1 + i][y_2] = matrix[x_1][y_1 + i]
            # 4=>1
            print("4=>1:", matrix[x_1][y_1 + i], "=", temp)
            matrix[x_1][y_1 + i] = temp
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 正方形矩阵的长和宽记为N(4)
        N = len(matrix)
        # 对于正方形的每一层，进行旋转
        # 每一层的左上角位置是记为(x_1,y_1)
        x_1, y_1 = 0, 0
        # 每一层右下角位置记为(x_2,y_2)
        x_2, y_2 = N - 1, N - 1

        # 对每一层调用rotateLayer函数
        while x_1 < x_2:
            # 只改变一层
            matrix = self.rotateLayer(matrix, x_1, y_1, x_2, y_2)
            x_1 += 1
            y_1 += 1
            x_2 -= 1
            y_2 -= 1


# @lc code=end
