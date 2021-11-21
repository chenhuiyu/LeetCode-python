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
                return True

            # 如果board[i][j]和word[k]上的字符不同，肯定走不出来word，剪枝返回false
            if board[i][j] != word[k]:
                return False

            # 判断i,j在四个方向上走，有一个是TRUE就返回true


# @lc code=end
