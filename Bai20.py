# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:54:25 2024

@author: KieuOanh
"""

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
if c > b and c > a:
    print("Giá trị lớn nhất là:", c)
elif b > a:
    print("Giá trị lớn nhất là:", b)
else:
    print("Giá trị lớn nhất là:", a)