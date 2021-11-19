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
            pre_string = res[i - 1]
            ans = []
            for char_index, char in enumerate(pre_string):
                if char_index == 0 or char != pre_string[char_index - 1]:
                    char_repeat = 1
                else:
                    char_repeat += 1
                ans.append(char_repeat, char)
            res[i] = ans.join("")
            print(res[i])


# @lc code=end
