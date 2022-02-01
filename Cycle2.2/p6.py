# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 17:48:45 2022

@author: Asus
"""

#6. Write a program to find out the value of X using solve(), given A and b .

import numpy as np
A=np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
b=np.array([[3],
             [5],
             [-2]])
inv=np.linalg.inv(A)
x=np.linalg.solve(inv,b)
print(x)