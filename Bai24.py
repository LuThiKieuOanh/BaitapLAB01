# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:46:16 2024

@author: KieuOanh
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
if h < 0 or h >23:
    print("Giờ không hợp lệ!")
elif m < 0 or m > 59 :
    print("Phút không hợp lệ!")
elif s < 0 or s > 59:
    print("Giây không hợp lệ!")
else:
    print("Giờ,phút và giây đều hợp lệ!")