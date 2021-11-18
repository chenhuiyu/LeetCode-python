'''
Date: 2021-10-18 11:49:45
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 11:51:43
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\1.两数之和.py
'''

#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return hashmap[target - num], index
            else:
                hashmap[num] = index


# @lc code=end
