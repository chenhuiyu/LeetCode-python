'''
Date: 2021-10-18 16:07:17
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 16:58:35
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
        if s == '':
            return 0
        hashmap = {}
        pre_longest_index = -1
        # longest_i = []
        longest = -1
        for index, char in enumerate(s):
            # hashmap中记录字符上一次出现的位置
            if char not in hashmap:
                last_repeat_index = -1
            else:
                last_repeat_index = hashmap[char]
            hashmap[char] = index
            longest_index = max(pre_longest_index, last_repeat_index)
            longest = max(longest, index - longest_index)
            # longest_i.append(index - longest_index)
            pre_longest_index = longest_index
        return max(longest_i)


# @lc code=end