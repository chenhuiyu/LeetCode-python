#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#


# @lc code=start
class Solution:
    def printOneLayer(self,matrix,x_1, y_1, x_2, y_2):
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        x_1, y_1 = 0, 0
        x_2, y_2 = n - 1, n - 1

        while x_1 <= x_2:
            self.printOneLayer(matrix,x_1, y_1, x_2, y_2)


    
# @lc code=end
