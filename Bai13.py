# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:33:34 2024

@author: KieuOanh
"""

ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{thang}/{ngay}")