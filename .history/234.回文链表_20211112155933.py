'''
Date: 2021-11-12 15:40:36
LastEditors: Chenhuiyu
LastEditTime: 2021-11-12 15:59:32
FilePath: \\.leetcode\\234.回文链表.py
'''

#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list = []
        cur = head
        while cur is not None:
            list.append(cur.val)
            cur = cur.next
        cur = head
        while len(list) > 0:
            if list.pop() != cur.val:
                return False
            cur = cur.next
        return True


# 快慢指针找中点优化版
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # slow在中点位置
        half_list = []
        while slow is not None:
            half_list.append(slow.val)
            slow = slow.next
        cur = head
        while len(half_list) > 0:
            if half_list.pop() != cur.val:
                return False
            cur = cur.next
        return True


# @lc code=end
