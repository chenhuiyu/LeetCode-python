'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-17 21:47:41
FilePath: \\.leetcode\\test.py
'''


def add(a, b):
    # 无进位相加
    sum = a

    # 进位
    cur = (a & b) << 1
    while (b != 0):
        sum = a ^ b
        cur = c & cur
