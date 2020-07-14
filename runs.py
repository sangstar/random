#!/usr/bin/env python
# coding: utf-8

# Author: Sanger Steel

import numpy as np




def runs_test(arr):
    runs = 0
    arr = list(arr)
    n1 = arr.count(1)
    n2 = arr.count(0)
    runs_exp = (2*n1*n2)/(n1+n2) + 1
    sr = ((2*n1*n2)*(2*n1*n2-n1-n2))/((n1+n2)**2 * (n1+n2-1))
    
    for i in range(len(arr) -1):
        current = arr[i]
        while arr[i+1] != current:
            runs+=1
            break
        runs+=1 
        Z = (runs - runs_exp)/np.sqrt(sr)
        return Z




arr = [1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0]




runs_test(arr)

