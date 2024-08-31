# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:06:08 2024

@author: KieuOanh
"""

a=int(input("Nhập a = "))
b=int(input("Nhập b = "))
c=int(input("Nhập c = "))
d=int(input("Nhập d = "))
sonhonhat=a
if b<a:
    a=b
if c<a:
    a=c
if d<a:
    a=d
print("Số nhỏ nhất là: ",sonhonhat)