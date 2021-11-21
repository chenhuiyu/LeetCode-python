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


# @lc code=end
