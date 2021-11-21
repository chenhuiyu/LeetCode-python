#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 正方形矩阵的长和宽记为N
        N = len(matrix)
        # 对于正方形的每一层，进行旋转
        # 每一层的左上角位置是记为(x_1,y_1)
        x_1, y_1 = 0, 0
        # 每一层右下角位置记为(x_2,y_2)
        x_2, y_2 = N - 1, N - 1
        # 对每一层调用rotateLayer函数


        def rotateLayer()


# @lc code=end
