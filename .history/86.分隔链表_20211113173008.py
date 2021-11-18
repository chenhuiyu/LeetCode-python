'''
Date: 2021-11-13 17:17:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 17:29:11
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
        # 小于区域头尾节点
        sH = None
        sT = None
        # 等于区域头尾结点
        eH = None
        eT = None
        # 大于区域头尾结点
        bH = None
        bT = None


# @lc code=end
