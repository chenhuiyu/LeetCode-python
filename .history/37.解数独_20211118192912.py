#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 计算限制数组
        row = [[0 for i in range(9)] for j in range(9)]
        col = [[0 for i in range(9)] for j in range(9)]
        bucket = [[0 for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                k = 3 * (i // 3) + j // 3
                if board[i][j] != ".":
                    num = int(board[i][j])
                    row[i][num - 1] = 1
                    col[j][num - 1] = 1
                    bucket[k][num - 1] = 1

        def processing(board,i,j,row,col,bucket):
            # 如果来到最后一个，返回true
            if i===9 and j==9:
                return True
            # 不需要填
            if board[i][j]=='.':
                



# @lc code=end
