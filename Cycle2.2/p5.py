# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:46:24 2022

@author: Asus
"""

#5. Write a program to check whether given matrix is symmetric or Skew Symmetric.


import numpy as np


A=np.array([[2,3,6],[3,4,5],[6,5,9]])
B=np.array([[0,2,9],[-2,0,3],[-9,-3,0]])
AT=A.transpose()
comparison = A == AT
equal_arrays = comparison.all()
print(equal_arrays)
m=(B.transpose() == -B).all()
print(m)
