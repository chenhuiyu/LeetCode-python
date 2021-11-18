'''
Date: 2021-11-15 02:50:54
LastEditors: Chenhuiyu
LastEditTime: 2021-11-17 21:55:09
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


def negNum(n):
    return add(~n, 1)


def minus(a, b):
    add(a, negNum(b))


if __name__ == "__main__":
    for i in range(100):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        print(add(a, b), a + b)
