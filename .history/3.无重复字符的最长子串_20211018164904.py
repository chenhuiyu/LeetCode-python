'''
Date: 2021-10-18 16:07:17
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 16:48:31
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\3.无重复字符的最长子串.py
'''

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        pre_longest_index = 0
        ans = []
        for index, char in enumerate(s):
            if char not in hashmap:
                last_repeat_index = -1
                hashmap[char] = index
            else:
                last_repeat_index = hashmap[char]
            longest_index = max(pre_longest_index, last_repeat_index)
            pre_longest_index = longest_index


# @lc code=end
