# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:42:07 2024

@author: KieuOanh
"""

a=float(input("Nhập a = "))
b=float(input("Nhập b = "))
if a==0 and b==0:
    print("Phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    x=-b/a
    print("Phương trình có nghiệm: ",x)