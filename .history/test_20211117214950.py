'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-17 21:49:49
FilePath: \\.leetcode\\test.py
'''
import random


def add(a, b):
    sum = a
    while (b != 0):
        # 无进位相加
        sum = a ^ b
        # 进位
        b = (a & b) << 1
        a = sum
    return sum


if __name__ == "__main__":
    a = random.randint(-100000, 100000)
    b = random.randint(-100000, 100000)
    print(add(a, b), a + b)
