#!/usr/bin/env python3
import numpy as np
#import math

# from numpy import linalg as LA

arr = [i for i in range(1,1000)]

# Proposed optimization: Replaced for loops with vectorized operations, which are much faster.
def doit1(x):
    x = np.arange(1, 100001)**2
    y1 = np.arange(1, 200001)**2
    z1 = np.arange(1, 300001)
    z = np.multiply(x[-1], y1[-1])
    return z

def doit2(x):
    i = 0
#    zarr = [math.cos(13) for i in range(1,100000)]
#    z = zarr[0]
    z = 0.1
    while i < 100000:
#        z = math.cos(13)
#        z = np.multiply(x,x)
#        z = np.multiply(z,z)
#        z = np.multiply(z,z)
        z = z * z
        z = x * x
        z = z * z
        z = z * z
        i += 1
    return z

def doit3(x):
    z = x + 1
    z = x + 1
    z = x + 1
    z = x + z
    z = x + z
#    z = np.cos(x)
    return z

def stuff():
#    y = np.random.randint(1, 100, size=50000000)[49999999]
    x = 1.01
    for i in range(1,10):
        print(i)
        for j in range(1,10):
            x = doit1(x)
            x = doit2(x)
            x = doit3(x)
            x = 1.01
    return x

import sys
print("TESTME")
print(sys.argv)
stuff()

