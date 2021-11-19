#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row[i][num]表示在第i行num数字是否出现
        row = [[0 for i in range(9)] for j in range(9)]
        # col[j][num]表示在第j列num数字是否出现
        col = [[0 for i in range(9)] for j in range(9)]
        # backet[k][num]表示在第k个宫内num数字是否出现
        backet = [[0 for i in range(9)] for j in range(9)]

        # 遍历整个数独
        # 第i行
        for i in range(9):
            # 第j列
            for j in range(9):
                # 通过行列计算求得现在处在第几个宫:
                k = 3 * (i // 3) + j // 3
                if board[i][j]


# @lc code=end
