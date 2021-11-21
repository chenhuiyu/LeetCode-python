#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
ord("z") - ord("A")


# @lc code=start
class Solution:
    def get_index:(self,char):
            if char.isupper():
                char_index = ord(char.lower()) - ord("a") + 26
                debit[char_index] += 1
            else:
                char_index = ord(char) - ord("a")
                debit[char_index] += 1
        return index

    def minWindow(self, s: str, t: str) -> str:
        # 如果t比s长，直接返回空串
        if len(s) < len(t):
            return ""
        # 建立一个26*2的英文字母对应表，表示每个字母的欠债情况
        debit = [0 for i in range(26 * 2)]
        # 根据被匹配字符t，初始化debit的欠债情况
        for char in t:
            if char.isupper():
                char_index = ord(char.lower()) - ord("a") + 26
                debit[char_index] += 1
            else:
                char_index = ord(char) - ord("a")
                debit[char_index] += 1
        # 总欠债情况
        count = len(t)

        # 使用双指针，left、right均初始化在0位置
        left = 0
        right = 0
        # right指针逐渐右扩，并且根据s中的值更新欠债表。
        while right<len(s):
            if 


# @lc code=end
