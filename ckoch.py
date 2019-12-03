# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from cmath import *
from IPython import display

def flist(f,lista):
    return list(map(f,lista))

def koch(n):
    rot = rect(1,pi/3) # complex(1/2,sqrt(3)/2)
    if n<=0:
        return [1/3,complex(1/2,sqrt(3)/6),2/3,1]
    else:
        k=koch(n-1)
        nkoch=flist(lambda z: z/3,k)
        nkoch+=flist(lambda z: 1/3+rot*z/3,k)
        nkoch+=flist(lambda z: complex(1/2,sqrt(3)/6)+z/3/rot,k)
        nkoch+=flist(lambda z: 2/3+z/3,k)
        return nkoch

rr=sqrt(3).real/3

def koch2(n):
    # Två steg i denna är ekvivalent med ett steg i koch 
    # koch2(2*n+1) ~ koch(n)
    rot = rect(1,pi/3) # complex(1/2,sqrt(3)/2)
    if n<=0:
        return [complex(1/2,sqrt(3)/6),1]
    else:
        k=koch2(n-1)
        kk1=flist(lambda z: z.conjugate()*rect(rr,pi/6),k)
        kk2=flist(lambda z : complex(1/2,sqrt(3)/6)+z.conjugate()*rect(rr,-pi/6),k)
        return kk1+kk2



#def svglist(clista):
    

def makesvg(n,size=1000,alg=1):
    if alg==2:
        k=[0]+koch2(n)
    else:
        k=[0]+koch(n)
        
    s=size
    polystr=''
    for c in k:
        x,y=c.real,c.imag
        st=str(int(s*x))+','+str(int(s/2-s*y))
        polystr+=st+' '
    bepa='<polyline points="'+polystr+'" style="fill:none;stroke:black;stroke-width:1"/>'
    apa='<svg width="{w}" height="{w}">'.format(w=size,h=size/2)+bepa+'</svg>'
    return apa


def makesvg2(n,size=1000,alg=1):
    if alg==2:
        k=[0]+koch2(n)
    else:
        k=[0]+koch(n)
        
    s=1
    polystr=''
    for c in k:
        x,y=c.real,c.imag
        st=str(s*x)+','+str(s*(1/3-y))
        polystr+=st+' '
    bepa='<polyline points="'+polystr+'" style="fill:none;stroke:black;stroke-width:{sw}"/>'.format(sw=1/size)
  #  apa='<svg width="{w}" height="{h}" viewbox="0 0 1 1">'.format(w=size,h=size/3)+bepa+'</svg>'
    apa='<svg width="{w}" height="{h}">'.format(w=size,h=size/3)+'<g transform="scale({sx},{sy})">'.format(sx=size,sy=size)+bepa+'</g></svg>'
    return apa

d=display.SVG(makesvg2(2,size=300))
