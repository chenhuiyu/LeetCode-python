'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-17 21:47:41
FilePath: \\.leetcode\\test.py
'''


def add(a, b):
    # 无进位相加
    sum = a
    c = a ^ b
    # 进位
    cur = (a & b) << 1
    while (cur != 0):
        c = cur ^ c
        cur = c & cur
