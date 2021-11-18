'''
Date: 2021-11-13 17:17:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 17:44:39
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
        # 大于区域头尾结点
        bH = None
        bT = None
        # next指针标记位置
        next = head
        while next is not None:
            next = head.next
            if head.val < x:
                if sH is None and sT is None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            else:
                if 


# @lc code=end
