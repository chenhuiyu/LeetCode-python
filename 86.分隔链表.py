'''
Date: 2021-11-13 17:17:58
LastEditors: Chenhuiyu
LastEditTime: 2021-11-13 17:49:21
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
            head.next = None
            if head.val < x:
                if sH is None and sT is None:
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            else:
                if bH is None and bT is None:
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            # 节点指向下一个
            head = next
        # 将小于区域的尾指针和大于区域的头指针串起来
        # 判断小于区域是否存在
        if sH is None and sT is None:
            return bH
        # 判断大于区域是否存在
        if bH is None and bT is None:
            return sH
        sT.next = bH
        return sH


# @lc code=end
