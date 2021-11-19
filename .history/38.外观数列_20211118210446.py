#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["0" for i in range(n)]
        res[1] = "1"
        for i in range(2, n):
            for char in range(res[i - 1]):
                num = 1


# @lc code=end
