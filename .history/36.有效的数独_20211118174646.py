#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row[i][num]表示在第i行num数字是否出现
        row = [[0] * 9] * 10


# @lc code=end
