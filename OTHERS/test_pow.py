# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:22:14 2017

@author: KAI
"""
import sys;
def pow(x,n):
    if n==1:
        return x
    elif n==0:
        return 0
    if n%2==0:
        return pow(x*x,n/2)
    else:
        return pow(x*x,(n-1)/2)*x


if __name__=='__main__':
    print(pow(9,6))