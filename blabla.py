#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 20:02:38 2019

@author: stefan
"""

from cmath import *
from IPython import display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

bild=np.array([
      [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]],
      [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]],
      [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]],
      [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]],
      [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
      [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
      [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]],
      [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
      ],dtype=np.float32)

psim=np.array([
        [0,1,2,3,4,5,6,7],
        [1,2,3,4,5,6,7,8],
        [2,3,4,5,6,7,8,9],
        [3,4,5,6,7,8,9,10]
        ])


imgplot = plt.imshow(bild)
imgplot = plt.imshow(psim,cmap='hot')

def carray(cmin,cmax,cd):
    c0=cmin
    dx=cd.real
    dy=cd.imag
    rows=[]
    escrows=[]
    cr=c0
    while cr.imag<=cmax.imag:
        row=[]
        escrow=[]
        c=cr
        while c.real<=cmax.real:
            row.append(c)
            escrow.append(escapetime(c))
            c+=dx
        rows.append(row)
        escrows.append(escrow)
        cr+=dy*1j
        
    #return(np.array(rows.reverse()))
    rows.reverse()
    escrows.reverse()
    return rows,escrows



def escapetime(c):
    z=c
    n=0
    nmax=100
    while abs(z)<=2:
        n+=1
        z=z**2+c
        if n>=nmax: break
    return n
    
