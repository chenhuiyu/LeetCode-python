#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 从board的i,j位置开始，是否能走出word
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                process(board, word, i, j, 0)

        def process(board, word, i, j, k):
            # 从board的i,j位置是否能走出word[k:]的部分

            # base case
            # k来到word终止位置，完整走出来了word，返回true
            if k == len(word):
                return true


# @lc code=end
