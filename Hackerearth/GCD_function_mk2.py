#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 01:13:54 2021

@author: digvijay
"""
xset=[0,1]
#xset.append(1)

def LCM(a,b):
    #b has to be bigger and a has to be smaller
    lcm=a*b
    for i in range(lcm-b , (b-1),-b):
        if i%a==0 and i%b==0:
            lcm=i;                
        
    return lcm

def xvalue(n):
    fn=1
    for x in range(2,n+1):
        fn=fn+x
        xset.append(LCM(x,xset[x-1]))        
        
    return xset[n],fn

i=int(input())
for s in range(i):
    n=int(input())
    if(n==1):
        print(1,1)
        continue
    x , fn =xvalue(n)    
    xset=[0,1]
    print(int(fn),x)