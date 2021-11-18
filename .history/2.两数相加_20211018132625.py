'''
Date: 2021-10-18 11:57:40
LastEditors: Chenhuiyu
LastEditTime: 2021-10-18 13:25:55
FilePath: \\leetcode_pythonc:\\Users\\Administrator\\.leetcode\\2.两数相加.py
'''

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        while l1 != None:
            list1.append(l1)
            l1 = l1.next
        while l2 != None:
            list2.append(l2)
            l2 = l2.next


# @lc code=end
