'''
Date: 2021-11-13 17:17:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 17:18:16
FilePath: \\.leetcode\\86.分隔链表.py
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
# @lc code=end

