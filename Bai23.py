# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:43:00 2024

@author: KieuOanh
"""

import math
a=float(input("Nhập a (khác 0)= "))
b=float(input("Nhập b = "))
c=float(input("Nhập c = "))
delta=b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    x=-b/2*a
    print("Phương trình có nghiệm duy nhất là: ",x)
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("Phương trình có nghiệm x1: ",x1)
    print("Phương trình có nghiệm x2: ",x2)