#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
ord("z")-ord("A")

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 如果t比s长，直接返回空串
        if len(s)<len(t):
            return ""
        # 建立一个26*2的英文字母对应表，表示每个字母的欠债情况
        debit = [0 for i in in range(26 * 2)]
        # 根据被匹配字符t，初始化debit的欠债情况
        for char in t:
            if char.inupper():
                debit[ord(char.lower())-ord("a")+26] = char
            else:
                debit[ord(char)-ord("a")]+=1


# @lc code=end
