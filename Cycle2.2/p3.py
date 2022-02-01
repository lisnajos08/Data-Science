# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:43:55 2022

@author: Asus
"""

#3. Multiply a matrix with a submatrix of another matrix and replace the same in larger matrix.

import numpy as np

np.random.seed(42)
m1=np.random.randint(0, 10, size=(5,6))
m2=np.random.randint(0, 10, size=(3,3))

print("matrix A :")
print(m1) 
print("shape :",m1.shape)
print("\nmatrix B :")
print(m2) 
print("shape :",m2.shape)

m3=m1[1:4,2:5] @ m2
m1[1:4,2:5]=m3

print("\nmatrix A after submatrix multiplication :")
print(m1)
print("shape :",m1.shape)