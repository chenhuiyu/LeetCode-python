'''
Date: 2021-11-12 15:40:36
LastEditors: Chenhuiyu
LastEditTime: 2021-11-12 15:42:59
FilePath: \\.leetcode\\234.回文链表.py
'''

#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list = []
        while head.next is not None:
            list.append(head.val)
            head = head.next


# @lc code=end
