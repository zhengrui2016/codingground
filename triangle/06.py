#! /user/bin/env python
# _*_  coding: utf-8  _*_
# __author__ = "王顶"
# Email: 408542507@qq.com

"""
终极金字塔
"""

def triangle(maxLevel = 4):
    level = 0
    while level < maxLevel:
        n = level * 2 + 1  # n 代表* 的个数
        m = maxLevel - level  # m 代表空格个数
        print(' ' * m + '*' * n)
        level = level + 1


num = input("input level(default 4):")
if num.isnumeric():
    n = int(num)
    if n>10:
        print('too big, no money!')
    elif n<3:
        print('too small, no room!')
    else:
        triangle(n)

if len(num) == 0:
    triangle()

if num.isalpha():
    print("input number between 3 and 10")
